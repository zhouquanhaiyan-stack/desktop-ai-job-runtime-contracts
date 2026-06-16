# Desktop AI Job Runtime Contracts — contracts.py
#
# Core enumerations and dataclasses that define the contract surface
# for desktop AI job execution, artifact tracking, and runtime adapters.

from __future__ import annotations

import enum
from dataclasses import dataclass, field
from typing import Dict, List


class JobType(enum.Enum):
    AUDIO = "audio"
    IMAGE = "image"
    VIDEO = "video"
    TEXT = "text"
    GENERIC = "generic"

    def __str__(self) -> str:
        return self.value


class JobStatus(enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELED = "canceled"

    def __str__(self) -> str:
        return self.value


class ArtifactKind(enum.Enum):
    PREVIEW = "preview"
    EXPORT = "export"
    LOG = "log"
    TRACE = "trace"
    MANIFEST = "manifest"

    def __str__(self) -> str:
        return self.value


class RuntimeCapability(enum.Enum):
    LOCAL_EXECUTION = "local_execution"
    DRY_RUN = "dry_run"
    TRACE_EVENTS = "trace_events"
    EXPORT_POLICY = "export_policy"
    ARTIFACT_MANIFEST = "artifact_manifest"

    def __str__(self) -> str:
        return self.value


@dataclass
class JobInput:
    input_id: str
    path: str
    media_type: str
    metadata: Dict[str, str] = field(default_factory=dict)


@dataclass
class JobArtifact:
    artifact_id: str
    kind: ArtifactKind
    path: str
    media_type: str
    metadata: Dict[str, str] = field(default_factory=dict)


@dataclass
class RuntimeAdapterInfo:
    adapter_id: str
    name: str
    version: str
    capabilities: List[RuntimeCapability] = field(default_factory=list)
