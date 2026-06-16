# Desktop AI Job Runtime Contracts
#
# Runtime contracts, job manifests, adapter boundaries, execution tracing,
# and export guard stubs for local desktop AI tools.
#
# This package provides the type definitions and orchestration layer
# for running AI jobs in a local desktop environment. It is intentionally
# dependency-free and suitable for public open-source use.

from .contracts import JobType, JobStatus, ArtifactKind, RuntimeCapability
from .contracts import JobInput, JobArtifact, RuntimeAdapterInfo
from .manifest import JobManifest, from_dict, to_dict, load_manifest, save_manifest, validate_manifest
from .trace import TraceEvent, ExecutionTrace
from .export_guard import ExportDecision, ExportGuard
from .adapter import BaseRuntimeAdapter, FakeRuntimeAdapter
from .runner import run_job

__all__ = [
    "JobType", "JobStatus", "ArtifactKind", "RuntimeCapability",
    "JobInput", "JobArtifact", "RuntimeAdapterInfo",
    "JobManifest", "from_dict", "to_dict", "load_manifest", "save_manifest",
    "validate_manifest",
    "TraceEvent", "ExecutionTrace",
    "ExportDecision", "ExportGuard",
    "BaseRuntimeAdapter", "FakeRuntimeAdapter",
    "run_job",
]
