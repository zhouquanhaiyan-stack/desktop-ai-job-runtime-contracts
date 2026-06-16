# Desktop AI Job Runtime Contracts — runner.py
#
# Top-level orchestration: load a manifest, run it through an adapter,
# persist results and trace, and return the final manifest.

from __future__ import annotations

from pathlib import Path
from typing import Optional

from .manifest import load_manifest, save_manifest, validate_manifest
from .trace import ExecutionTrace
from .adapter import FakeRuntimeAdapter
from .manifest import JobManifest


def run_job(
    manifest_path: str | Path,
    output_dir: Optional[str | Path] = None,
) -> JobManifest:
    """Run a desktop AI job given a manifest file.

    Args:
        manifest_path: Path to the JSON manifest file.
        output_dir: Override for the manifest's output directory.

    Returns:
        The final JobManifest with updated status and artifacts.
    """
    manifest = load_manifest(manifest_path)
    validate_manifest(manifest)

    if output_dir is not None:
        manifest.output_dir = str(output_dir)

    out_path = Path(manifest.output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    trace = ExecutionTrace(job_id=manifest.job_id)
    adapter = FakeRuntimeAdapter()
    manifest = adapter.run(manifest, trace)

    save_manifest(manifest, out_path / "result_manifest.json")
    trace.save_trace(out_path / "execution_trace.json")

    return manifest
