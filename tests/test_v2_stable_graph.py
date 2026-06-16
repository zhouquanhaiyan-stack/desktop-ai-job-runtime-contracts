import unittest
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent
_SRC = _REPO_ROOT / "src"

import sys
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from desktop_ai_job_runtime_contracts import JobInput, JobManifest, JobStatus, JobType
from desktop_ai_job_runtime_contracts.execution_graph import (
    ExecutionGraph,
    build_graph_from_manifest,
)


class TestV2StableGraph(unittest.TestCase):

    def setUp(self):
        self.manifest = JobManifest(
            job_id="stable-graph-job",
            job_type=JobType.TEXT,
            inputs=[
                JobInput(
                    input_id="in-1",
                    path="input.txt",
                    media_type="text/plain",
                )
            ],
            output_dir="out/stable-graph-job",
            status=JobStatus.PENDING,
        )

    def test_graph_always_has_three_nodes(self):
        graph = build_graph_from_manifest(self.manifest)
        self.assertEqual(len(graph.nodes), 3)

    def test_nodes_include_stable_stages(self):
        graph = build_graph_from_manifest(self.manifest)
        stages = [node.stage for node in graph.nodes]
        self.assertEqual(stages, ["scan", "execute", "finalize"])

    def test_build_graph_from_manifest_returns_execution_graph(self):
        graph = build_graph_from_manifest(self.manifest)
        self.assertIsInstance(graph, ExecutionGraph)

    def test_manifest_to_execution_graph(self):
        graph = self.manifest.to_execution_graph()
        self.assertIsInstance(graph, ExecutionGraph)
        self.assertEqual([node.node_id for node in graph.nodes], ["scan", "execute", "finalize"])


if __name__ == "__main__":
    unittest.main()
