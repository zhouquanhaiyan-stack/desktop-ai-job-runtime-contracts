# Desktop AI Job Runtime Contracts - runtime_spec_v3.py
#
# Declarative v3 runtime specification. This module contains no execution
# logic and does not modify runtime behavior.

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass(frozen=True)
class RuntimeSpecV3:
    version: str = "v3"
    contract_name: str = "desktop-ai-job-runtime-contracts"
    execution_model: str = "deterministic_scan_execute_finalize"
    graph_model: Dict[str, Any] = field(default_factory=lambda: {
        "type": "deterministic_dag",
        "stages": ["scan", "execute", "finalize"],
        "edges": [
            {"from": "scan", "to": "execute"},
            {"from": "execute", "to": "finalize"},
        ],
        "dynamic_branching": False,
    })
    trace_model: Dict[str, Any] = field(default_factory=lambda: {
        "type": "append_only_event_log",
        "event_fields": [
            "event_id",
            "timestamp",
            "stage",
            "message",
            "metadata",
            "event_type",
        ],
        "event_types": [
            "GRAPH_BUILD",
            "ADAPTER_START",
            "ADAPTER_EXECUTE",
            "ARTIFACT_WRITE",
            "ADAPTER_END",
        ],
    })
    artifact_model: Dict[str, Any] = field(default_factory=lambda: {
        "type": "typed_outputs",
        "artifact_types": ["preview", "log", "trace", "manifest"],
        "required_fields": [
            "artifact_id",
            "kind",
            "path",
            "media_type",
            "metadata",
        ],
    })
    adapter_model: Dict[str, Any] = field(default_factory=lambda: {
        "type": "isolated_runtime_adapter",
        "included_adapter": "FakeRuntimeAdapter",
        "execution_logic_defined_here": False,
    })


def get_runtime_spec_v3() -> RuntimeSpecV3:
    return RuntimeSpecV3()
