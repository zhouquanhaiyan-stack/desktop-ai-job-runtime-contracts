# Desktop AI Job Runtime Contracts - execution_graph.py
#
# Deterministic execution graph structures for the v2 runtime contract layer.

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class ExecutionNode:
    node_id: str
    stage: str
    depends_on: List[str] = field(default_factory=list)


@dataclass
class ExecutionGraph:
    nodes: List[ExecutionNode]


def build_graph_from_manifest(manifest: object) -> ExecutionGraph:
    """Build the stable v2 graph for a job manifest.

    The graph is intentionally static: every manifest maps to scan, execute,
    and finalize in that order. The manifest object is accepted to keep the
    builder anchored to the runtime contract without introducing branching.
    """
    return ExecutionGraph(
        nodes=[
            ExecutionNode(node_id="scan", stage="scan", depends_on=[]),
            ExecutionNode(node_id="execute", stage="execute", depends_on=["scan"]),
            ExecutionNode(node_id="finalize", stage="finalize", depends_on=["execute"]),
        ]
    )
