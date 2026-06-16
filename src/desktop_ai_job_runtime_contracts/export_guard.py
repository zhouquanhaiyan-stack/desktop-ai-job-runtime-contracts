# Desktop AI Job Runtime Contracts — export_guard.py
#
# Generic export policy guard with sample plan tiers (free / plus / pro).
# This is a *demonstration* stub only. It does not contain any real
# licensing, payment, or authorization logic.

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from .contracts import ArtifactKind


@dataclass
class ExportDecision:
    allowed: bool
    reason: str
    plan_name: str
    artifact_kind: ArtifactKind


class ExportGuard:
    """Sample export guard that enforces artifact-kind policies per plan tier.

    Plan tiers (illustrative only):
    - free: preview-only, no export
    - plus: preview + export allowed with a reminder
    - pro : all artifact kinds allowed
    - unknown: blocked
    """

    def __init__(self, plan_name: str = "free") -> None:
        self._plan_name = plan_name
        self._allowed: Dict[str, set[str]] = {
            "free": {"preview"},
            "plus": {"preview", "export"},
            "pro": {"preview", "export", "log", "trace", "manifest"},
        }

    def evaluate(self, plan_name: str, artifact_kind: ArtifactKind) -> ExportDecision:
        plan = plan_name.lower()
        kind_str = str(artifact_kind)
        allowed_kinds = self._allowed.get(plan)

        if allowed_kinds is None:
            return ExportDecision(
                allowed=False,
                reason=f"Unknown plan '{plan_name}'. Export blocked.",
                plan_name=plan_name,
                artifact_kind=artifact_kind,
            )

        if kind_str in allowed_kinds and plan == "plus" and kind_str == "export":
            return ExportDecision(
                allowed=True,
                reason=f"Plan '{plan_name}' allows limited export for {kind_str} artifacts.",
                plan_name=plan_name,
                artifact_kind=artifact_kind,
            )

        if kind_str in allowed_kinds:
            return ExportDecision(
                allowed=True,
                reason=f"Plan '{plan_name}' allows {kind_str} artifacts.",
                plan_name=plan_name,
                artifact_kind=artifact_kind,
            )

        return ExportDecision(
            allowed=False,
            reason=f"Plan '{plan_name}' does not allow {kind_str} artifacts.",
            plan_name=plan_name,
            artifact_kind=artifact_kind,
        )
