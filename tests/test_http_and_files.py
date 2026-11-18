"""Retry behavior of the provider HTTP layer and atomic file writes."""
import contextlib
import io
import json
import stat
import unittest
from email.message import Message
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
from urllib.error import HTTPError, URLError

from doc4cf.generator import request_with_retry, write_atomic


def http_error(code, body=b"{}", retry_after=None):
    headers = Message()
    if retry_after is not None:
        headers["Retry-After"] = retry_after
    return HTTPError("https://example.invalid", code, "error", headers, io.BytesIO(body))


def ok():
    return io.BytesIO(json.dumps({"ok": True}).encode())


class RequestRetry(unittest.TestCase):
    def run_retry(self, outcomes, **options):
        sleeps = []
        output = io.StringIO()
        with patch("doc4cf.generator.urlopen", side_effect=outcomes) as send, \
                patch("doc4cf.generator.time.sleep", sleeps.append), \
                contextlib.redirect_stdout(output):
            try:
                result = request_with_retry(object(), **options)
            except Exception as error:  # noqa: BLE001 - returned for assertions
                result = error
        return result, sleeps, output.getvalue(), send

    def test_retry_after_is_capped_at_max_delay(self):
        result, sleeps, _, _ = self.run_retry([http_error(429, retry_after="86400"), ok()], max_delay=120)
        self.assertEqual(result, {"ok": True})
        self.assertEqual(sleeps, [120])

    def test_rate_limit_body_is_logged_once(self):
        with self.assertLogs("doc4cf.generator", level="WARNING") as logs:
            self.run_retry([http_error(429, b'{"error": "slow down"}', "0"), ok()])
        self.assertIn("slow down", "\n".join(logs.output))

    def test_server_errors_are_retried(self):
        with self.assertLogs("doc4cf.generator", level="INFO") as logs:
            result, sleeps, _, send = self.run_retry([http_error(503, retry_after="1"), ok()])
        self.assertEqual(result, {"ok": True})
        self.assertEqual((send.call_count, sleeps), (2, [1.0]))
        self.assertIn("HTTP 503: retrying in 1.0 seconds", "\n".join(logs.output))

    def test_network_errors_are_retried(self):
        result, sleeps, _, send = self.run_retry([URLError("down"), ok()])
        self.assertEqual(result, {"ok": True})
        self.assertEqual((send.call_count, len(sleeps)), (2, 1))

    def test_client_errors_are_not_retried(self):
        result, sleeps, _, send = self.run_retry([http_error(401), ok()])
        self.assertIsInstance(result, HTTPError)
        self.assertEqual((send.call_count, sleeps), (1, []))

    def test_daily_quota_fails_fast(self):
        body = json.dumps({"error": {"metadata": {
            "limit_source": "openrouter_free_tier_daily",
            "headers": {"X-RateLimit-Reset": "1767225600000"}}}}).encode()
        result, sleeps, _, send = self.run_retry([http_error(429, body), ok()])
        self.assertIsInstance(result, RuntimeError)
        self.assertIn("quota exhausted", str(result))
        self.assertEqual((send.call_count, sleeps), (1, []))

    def test_gives_up_after_max_retries(self):
        result, _, _, send = self.run_retry([http_error(503)] * 3, max_retries=2)
        self.assertIsInstance(result, HTTPError)
        self.assertEqual(send.call_count, 3)


class AtomicWrite(unittest.TestCase):
    def test_mode_is_applied(self):
        with TemporaryDirectory() as tmp:
            public, private = Path(tmp) / "site.json", Path(tmp) / "cache.json"
            write_atomic(public, "{}")
            write_atomic(private, "{}", mode=0o600)
            self.assertEqual(stat.S_IMODE(public.stat().st_mode), 0o644)
            self.assertEqual(stat.S_IMODE(private.stat().st_mode), 0o600)

    def test_temporary_file_removed_when_replace_fails(self):
        with TemporaryDirectory() as tmp, patch.object(Path, "replace", side_effect=OSError("boom")):
            with self.assertRaises(OSError):
                write_atomic(Path(tmp) / "out.json", "{}")
            self.assertEqual(list(Path(tmp).iterdir()), [])


if __name__ == "__main__":
    unittest.main()
