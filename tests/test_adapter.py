import unittest
import tempfile
from pathlib import Path
from desktop_ai_job_runtime_contracts import (
    JobType, JobStatus, JobInput, ArtifactKind,
    JobManifest, ExecutionTrace,
    FakeRuntimeAdapter,
)


class TestFakeRuntimeAdapter(unittest.TestCase):

    def setUp(self):
        self.manifest = JobManifest(
            job_id="test-adapter-job",
            job_type=JobType.IMAGE,
            inputs=[
                JobInput(input_id="in-1", path="input.png", media_type="image/png"),
            ],
            output_dir="/tmp/fake-adapter-out",
            status=JobStatus.PENDING,
        )
        self.trace = ExecutionTrace(job_id=self.manifest.job_id)
        self.adapter = FakeRuntimeAdapter()

    def test_get_info(self):
        info = self.adapter.get_info()
        self.assertEqual(info.adapter_id, "fake-adapter-001")
        self.assertEqual(info.name, "FakeRuntimeAdapter")
        self.assertTrue(len(info.capabilities) > 0)

    def test_run_updates_status(self):
        result = self.adapter.run(self.manifest, self.trace)
        self.assertIs(result.status, JobStatus.SUCCEEDED)

    def test_run_creates_artifacts(self):
        result = self.adapter.run(self.manifest, self.trace)
        self.assertEqual(len(result.artifacts), 2)
        kinds = {a.kind for a in result.artifacts}
        self.assertIn(ArtifactKind.PREVIEW, kinds)
        self.assertIn(ArtifactKind.LOG, kinds)

    def test_run_adds_trace_events(self):
        self.adapter.run(self.manifest, self.trace)
        stages = [e.stage for e in self.trace.events]
        self.assertIn("adapter_started", stages)
        self.assertIn("input_scanned", stages)
        self.assertIn("artifact_created", stages)
        self.assertIn("adapter_finished", stages)

    def test_run_writes_output_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.manifest.output_dir = tmp
            self.adapter.run(self.manifest, self.trace)
            out = Path(tmp)
            self.assertTrue((out / "fake_preview.txt").exists())
            self.assertTrue((out / "fake_run.log").exists())

