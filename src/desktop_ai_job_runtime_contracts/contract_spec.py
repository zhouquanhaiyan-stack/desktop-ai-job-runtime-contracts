# Desktop AI Job Runtime Contracts - contract_spec.py
#
# Static schema holder for the v2 runtime contract layer.

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class ContractSpec:
    version: str
    job_fields: List[str]
    artifact_types: List[str]
    trace_events: List[str]


def get_spec_v2() -> ContractSpec:
    return ContractSpec(
        version="v2",
        job_fields=[
            "job_id",
            "job_type",
            "inputs",
            "output_dir",
            "status",
        ],
        artifact_types=[
            "preview",
            "log",
            "trace",
            "manifest",
        ],
        trace_events=[
            "GRAPH_BUILD",
            "ADAPTER_START",
            "ADAPTER_EXECUTE",
            "ARTIFACT_WRITE",
            "ADAPTER_END",
        ],
    )
