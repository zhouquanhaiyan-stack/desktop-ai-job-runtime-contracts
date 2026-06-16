import unittest
import tempfile
import json
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent
_SRC = _REPO_ROOT / "src"

import sys
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from desktop_ai_job_runtime_contracts import ExecutionTrace


class TestTrace(unittest.TestCase):

    def setUp(self):
        self.trace = ExecutionTrace(job_id="trace-test-job")

    def test_add_event_returns_event(self):
        event = self.trace.add_event("test_stage", "test message")
        self.assertEqual(event.stage, "test_stage")
        self.assertEqual(event.message, "test message")
        self.assertTrue(len(event.event_id) > 0)
        self.assertTrue(len(event.timestamp) > 0)

    def test_add_event_increments_list(self):
        self.trace.add_event("stage1", "msg1")
        self.trace.add_event("stage2", "msg2")
        self.assertEqual(len(self.trace.events), 2)

    def test_add_event_with_metadata(self):
        self.trace.add_event("stage", "msg", {"key": "val"})
        self.assertEqual(self.trace.events[0].metadata, {"key": "val"})

    def test_to_dict_structure(self):
        self.trace.add_event("stage", "msg")
        d = self.trace.to_dict()
        self.assertEqual(d["job_id"], "trace-test-job")
        self.assertEqual(len(d["events"]), 1)
        self.assertIn("event_id", d["events"][0])

    def test_save_trace(self):
        self.trace.add_event("stage", "msg")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "trace.json"
            self.trace.save_trace(path)
            self.assertTrue(path.exists())
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(data["job_id"], "trace-test-job")
            self.assertEqual(len(data["events"]), 1)