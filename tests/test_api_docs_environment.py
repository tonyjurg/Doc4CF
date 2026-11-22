"""Regression checks for api docs environment."""
import unittest
from pathlib import Path
from unittest import mock


class ApiDocsEnvironment(unittest.TestCase):
    def test_release_install_and_sphinx_receive_filtered_environments(self):
        import importlib.util
        import os
        spec = importlib.util.spec_from_file_location(
            "build_api_docs", Path(__file__).resolve().parents[1] / "scripts" / "build_api_docs.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        source, output = Path("source"), Path("output")
        env = {"PATH": "tools", "GH_TOKEN": "test-token", "mixed_Api_Key": "test-key",
               "DB_PASSWORD": "test-password", "CREDENTIAL_FILE": "test-file", "DOC4CF_TEST": "kept"}
        with mock.patch.dict(os.environ, env, clear=True), \
                mock.patch.object(module.venv, "EnvBuilder"), \
                mock.patch.object(module.subprocess, "run") as run:
            module.build_release(source, output, "v1", [{"label": "v1", "output": output}], [])
            self.assertEqual(os.environ["GH_TOKEN"], "test-token")
        self.assertEqual(run.call_count, 2)
        for call in run.call_args_list:
            child_env = call.kwargs["env"]
            for key in ("GH_TOKEN", "mixed_Api_Key", "DB_PASSWORD", "CREDENTIAL_FILE"):
                self.assertNotIn(key, child_env)
            self.assertEqual(child_env["PATH"], "tools")
            self.assertEqual(child_env["DOC4CF_TEST"], "kept")
        self.assertEqual(run.call_args.kwargs["env"]["DOC4CF_DOCS_VERSION"], "v1")

    def test_credentials_are_not_passed_to_release_code(self):
        import importlib.util
        import os
        spec = importlib.util.spec_from_file_location(
            "build_api_docs", Path(__file__).resolve().parents[1] / "scripts" / "build_api_docs.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with mock.patch.dict(os.environ, {"GH_TOKEN": "t", "MY_SECRET": "t"}):
            env = module.build_environment()
        self.assertNotIn("GH_TOKEN", env)
        self.assertNotIn("MY_SECRET", env)
        self.assertIn("PATH", env)


if __name__ == "__main__":
    unittest.main()
