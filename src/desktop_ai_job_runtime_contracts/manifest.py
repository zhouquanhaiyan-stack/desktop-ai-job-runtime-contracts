# Desktop AI Job Runtime Contracts — manifest.py
#
# Job manifest serialization, deserialization, validation, and file I/O.

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, List

from .contracts import JobType, JobStatus, JobInput, JobArtifact, ArtifactKind


@dataclass
class JobManifest:
    job_id: str
    job_type: JobType
    inputs: List[JobInput]
    output_dir: str
    status: JobStatus
    artifacts: List[JobArtifact] = field(default_factory=list)
    metadata: Dict[str, str] = field(default_factory=dict)

    def to_execution_graph(self) -> "ExecutionGraph":
        from .execution_graph import build_graph_from_manifest

        return build_graph_from_manifest(self)


def to_dict(manifest: JobManifest) -> Dict[str, Any]:
    d = asdict(manifest)
    d["job_type"] = str(manifest.job_type)
    d["status"] = str(manifest.status)
    for inp in d.get("inputs", []):
        inp["media_type"] = str(inp.get("media_type", ""))
    for art in d.get("artifacts", []):
        art["kind"] = str(art.get("kind", ""))
        art["media_type"] = str(art.get("media_type", ""))
    return d


def from_dict(data: Dict[str, Any]) -> JobManifest:
    job_type = JobType(data["job_type"])
    status = JobStatus(data["status"])
    inputs = [JobInput(**i) for i in data.get("inputs", [])]
    artifacts_raw = data.get("artifacts", [])
    artifacts = []
    for a in artifacts_raw:
        ak = ArtifactKind(a["kind"]) if "kind" in a else None
        artifacts.append(JobArtifact(
            artifact_id=a["artifact_id"], kind=ak,
            path=a["path"], media_type=a["media_type"],
            metadata=a.get("metadata", {}),
        ))
    return JobManifest(
        job_id=data["job_id"],
        job_type=job_type,
        inputs=inputs,
        output_dir=data["output_dir"],
        status=status,
        artifacts=artifacts,
        metadata=data.get("metadata", {}),
    )


def load_manifest(path: str | Path) -> JobManifest:
    data = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    return from_dict(data)


def save_manifest(manifest: JobManifest, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(to_dict(manifest), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def validate_manifest(manifest: JobManifest) -> None:
    if not manifest.job_id:
        raise ValueError("job_id must not be empty")
    if not isinstance(manifest.job_type, JobType):
        raise ValueError(f"Invalid job_type: {manifest.job_type}")
    if not manifest.inputs:
        raise ValueError("inputs must have at least one entry")
    for inp in manifest.inputs:
        if not inp.input_id:
            raise ValueError(f"input_id must not be empty: {inp}")
        if not inp.path:
            raise ValueError(f"path must not be empty for input {inp.input_id}")
        if not inp.media_type:
            raise ValueError(f"media_type must not be empty for input {inp.input_id}")
    if not manifest.output_dir:
        raise ValueError("output_dir must not be empty")
    if not isinstance(manifest.status, JobStatus):
        raise ValueError(f"Invalid status: {manifest.status}")
