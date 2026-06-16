import json
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent
_SRC = _REPO_ROOT / "src"

import sys
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from desktop_ai_job_runtime_contracts.specs.runtime_spec_v3 import (
    RuntimeSpecV3,
    get_runtime_spec_v3,
)


class TestV3Spec(unittest.TestCase):

    def test_get_runtime_spec_v3_returns_object(self):
        spec = get_runtime_spec_v3()
        self.assertIsInstance(spec, RuntimeSpecV3)

    def test_version_is_v3(self):
        spec = get_runtime_spec_v3()
        self.assertEqual(spec.version, "v3")

    def test_required_fields_exist(self):
        spec = get_runtime_spec_v3()
        self.assertTrue(spec.contract_name)
        self.assertTrue(spec.execution_model)
        self.assertIn("stages", spec.graph_model)
        self.assertIn("event_types", spec.trace_model)
        self.assertIn("artifact_types", spec.artifact_model)
        self.assertIn("included_adapter", spec.adapter_model)

    def test_schema_v3_json_is_valid_json(self):
        schema_path = _SRC / "desktop_ai_job_runtime_contracts" / "specs" / "schema_v3.json"
        data = json.loads(schema_path.read_text(encoding="utf-8"))
        self.assertEqual(data["version"], "v3")
        self.assertIn("job_manifest", data["schemas"])
        self.assertIn("execution_graph", data["schemas"])
        self.assertIn("trace_event", data["schemas"])
        self.assertIn("artifact", data["schemas"])

    def test_spec_is_immutable_like(self):
        spec = get_runtime_spec_v3()
        with self.assertRaises(FrozenInstanceError):
            spec.version = "changed"


if __name__ == "__main__":
    unittest.main()
