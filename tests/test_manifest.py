import unittest
import json
import tempfile
from pathlib import Path
from dataclasses import asdict
from desktop_ai_job_runtime_contracts import (
    JobType, JobStatus, JobInput, JobArtifact, ArtifactKind,
    JobManifest, from_dict, to_dict, load_manifest, save_manifest,
    validate_manifest,
)


class TestManifest(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            "job_id": "test-job-001",
            "job_type": "audio",
            "inputs": [
                {"input_id": "in-1", "path": "/tmp/in.wav", "media_type": "audio/wav", "metadata": {}},
            ],
            "output_dir": "/tmp/out/test-job-001",
            "status": "pending",
            "artifacts": [],
            "metadata": {"source": "test"},
        }

    def test_from_dict_roundtrip(self):
        manifest = from_dict(self.sample_data)
        self.assertEqual(manifest.job_id, "test-job-001")
        self.assertIs(manifest.job_type, JobType.AUDIO)
        self.assertIs(manifest.status, JobStatus.PENDING)
        self.assertEqual(len(manifest.inputs), 1)

        back = to_dict(manifest)
        self.assertEqual(back["job_type"], "audio")
        self.assertEqual(back["status"], "pending")
        self.assertEqual(back["job_id"], "test-job-001")

    def test_load_save_roundtrip(self):
        manifest = from_dict(self.sample_data)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "manifest.json"
            save_manifest(manifest, path)
            self.assertTrue(path.exists())

            loaded = load_manifest(path)
            self.assertEqual(loaded.job_id, manifest.job_id)
            self.assertIs(loaded.job_type, manifest.job_type)
            self.assertIs(loaded.status, manifest.status)

    def test_validate_valid(self):
        manifest = from_dict(self.sample_data)
        try:
            validate_manifest(manifest)
        except ValueError as e:
            self.fail(f"validate_manifest raised ValueError: {e}")

    def test_validate_empty_job_id(self):
        data = dict(self.sample_data, job_id="")
        manifest = from_dict(data)
        with self.assertRaises(ValueError):
            validate_manifest(manifest)

    def test_validate_empty_inputs(self):
        data = dict(self.sample_data, inputs=[])
        manifest = from_dict(data)
        with self.assertRaises(ValueError):
            validate_manifest(manifest)

    def test_validate_empty_output_dir(self):
        data = dict(self.sample_data, output_dir="")
        manifest = from_dict(data)
        with self.assertRaises(ValueError):
            validate_manifest(manifest)

    def test_validate_missing_input_fields(self):
        data = dict(self.sample_data, inputs=[{"input_id": "", "path": "", "media_type": "", "metadata": {}}])
        manifest = from_dict(data)
        with self.assertRaises(ValueError):
            validate_manifest(manifest)

    def test_to_dict_includes_artifacts(self):
        data = dict(self.sample_data, artifacts=[
            {"artifact_id": "art-1", "kind": "preview", "path": "/tmp/preview.txt", "media_type": "text/plain", "metadata": {}},
        ])
        manifest = from_dict(data)
        d = to_dict(manifest)
        self.assertEqual(len(d["artifacts"]), 1)
        self.assertEqual(d["artifacts"][0]["kind"], "preview")

