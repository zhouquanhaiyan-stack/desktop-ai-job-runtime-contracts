import unittest
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent
_SRC = _REPO_ROOT / "src"

import sys
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from desktop_ai_job_runtime_contracts import ArtifactKind, ExportDecision, ExportGuard


class TestExportGuard(unittest.TestCase):

    def setUp(self):
        self.guard = ExportGuard()

    def test_free_plan_allows_preview(self):
        decision = self.guard.evaluate("free", ArtifactKind.PREVIEW)
        self.assertTrue(decision.allowed)
        self.assertEqual(decision.plan_name, "free")

    def test_free_plan_blocks_export(self):
        decision = self.guard.evaluate("free", ArtifactKind.EXPORT)
        self.assertFalse(decision.allowed)

    def test_free_plan_blocks_log(self):
        decision = self.guard.evaluate("free", ArtifactKind.LOG)
        self.assertFalse(decision.allowed)

    def test_plus_plan_allows_preview(self):
        decision = self.guard.evaluate("plus", ArtifactKind.PREVIEW)
        self.assertTrue(decision.allowed)

    def test_plus_plan_allows_export_with_limited_reason(self):
        decision = self.guard.evaluate("plus", ArtifactKind.EXPORT)
        self.assertTrue(decision.allowed)
        self.assertIn("limited", decision.reason)

    def test_pro_plan_allows_all_kinds(self):
        for kind in ArtifactKind:
            decision = self.guard.evaluate("pro", kind)
            self.assertTrue(decision.allowed, f"pro plan should allow {kind}")

    def test_unknown_plan_blocks_all(self):
        decision = self.guard.evaluate("enterprise", ArtifactKind.EXPORT)
        self.assertFalse(decision.allowed)
        self.assertIn("Unknown", decision.reason)

    def test_unknown_plan_blocks_preview(self):
        decision = self.guard.evaluate("enterprise", ArtifactKind.PREVIEW)
        self.assertFalse(decision.allowed)