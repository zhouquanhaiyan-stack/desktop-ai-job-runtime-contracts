"""Tests for example manifests and example runner."""

import json
import tempfile
import unittest
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent
_SRC = _REPO_ROOT / "src"

import sys
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from desktop_ai_job_runtime_contracts.manifest import load_manifest, validate_manifest
from desktop_ai_job_runtime_contracts.contracts import JobStatus
from desktop_ai_job_runtime_contracts import run_job


class TestExampleManifests(unittest.TestCase):
    """Verify all example manifests load and validate."""

    def _test_manifest(self, name: str):
        path = _REPO_ROOT / "examples" / name
        self.assertTrue(path.exists(), f"Missing example manifest: {path}")
        manifest = load_manifest(str(path))
        validate_manifest(manifest)
        self.assertEqual(manifest.status, JobStatus.PENDING)

    def test_fake_audio_job(self):
        self._test_manifest("fake_audio_job.json")

    def test_fake_image_job(self):
        self._test_manifest("fake_image_job.json")

    def test_fake_text_job(self):
        self._test_manifest("fake_text_job.json")


class TestTextJobExecution(unittest.TestCase):
    """Run the text job example through the runtime and verify output."""

    def test_text_job_succeeds_with_artifacts(self):
        manifest_path = str(_REPO_ROOT / "examples" / "fake_text_job.json")

        with tempfile.TemporaryDirectory(prefix="text-job-test-") as tmpdir:
            result = run_job(manifest_path, output_dir=tmpdir)

            self.assertEqual(result.status, JobStatus.SUCCEEDED)
            self.assertGreaterEqual(len(result.artifacts), 2)

            json_path = Path(tmpdir) / "result_manifest.json"
            self.assertTrue(json_path.exists(), "result_manifest.json missing")
            with open(json_path, encoding="utf-8") as f:
                saved = json.load(f)
            self.assertEqual(saved["status"], "succeeded")