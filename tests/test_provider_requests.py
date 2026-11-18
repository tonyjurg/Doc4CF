"""Shared provider request construction tests."""
import unittest
from unittest.mock import patch

from doc4cf.providers import PROVIDERS, build_provider_request


class ProviderRequest(unittest.TestCase):
    def test_provider_endpoint_and_auth_headers_table(self):
        for provider, (_label, key_name, endpoint) in PROVIDERS.items():
            with self.subTest(provider=provider), patch.dict("os.environ", {key_name: "secret"}, clear=False):
                request = build_provider_request(provider, b'{"ok":true}', "--model")
                self.assertEqual(request.full_url, endpoint)
                self.assertEqual(request.data, b'{"ok":true}')
                self.assertEqual(request.get_header("Content-type"), "application/json")
                if provider == "anthropic":
                    self.assertEqual(request.get_header("X-api-key"), "secret")
                    self.assertEqual(request.get_header("Anthropic-version"), "2023-06-01")
                else:
                    self.assertEqual(request.get_header("Authorization"), "Bearer secret")

    def test_anthropic_workspace_header_is_optional(self):
        with patch.dict("os.environ", {"ANTHROPIC_API_KEY": "secret", "ANTHROPIC_WORKSPACE_ID": "workspace"}):
            request = build_provider_request("anthropic", b"{}", "--model")
        self.assertEqual(request.get_header("Anthropic-workspace-id"), "workspace")

    def test_missing_key_keeps_command_specific_guidance(self):
        for provider, (_, key_name, _) in PROVIDERS.items():
            with self.subTest(provider=provider), patch.dict("os.environ", {}, clear=True):
                with self.assertRaisesRegex(ValueError, rf"Set {key_name} or omit --analyze-context"):
                    build_provider_request(provider, b"{}", "--analyze-context")


if __name__ == "__main__":
    unittest.main()
