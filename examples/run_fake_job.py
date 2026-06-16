#!/usr/bin/env python3
"""Run a fake desktop AI job for demonstration purposes.

Usage:
    python examples/run_fake_job.py
    python examples/run_fake_job.py examples/fake_image_job.json
    python examples/run_fake_job.py examples/fake_text_job.json

This script works without installing the package by adding
the src directory to sys.path.
"""

import sys
import json
from pathlib import Path

# Allow running without installing the package
_repo_root = Path(__file__).resolve().parent.parent
_src = _repo_root / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from desktop_ai_job_runtime_contracts import run_job
from desktop_ai_job_runtime_contracts.manifest import load_manifest


def resolve_manifest_path(raw: str, repo_root: Path) -> Path:
    """Resolve a manifest path relative to the repo root or as an absolute path."""
    p = Path(raw)
    if p.is_absolute():
        return p
    return (repo_root / p).resolve()


def main() -> None:
    argc = len(sys.argv) - 1

    if argc == 0:
        manifest_name = "fake_audio_job.json"
        manifest_path = _repo_root / "examples" / manifest_name
        job_slug = "fake-audio-job-001"
    elif argc == 1:
        manifest_path = resolve_manifest_path(sys.argv[1], _repo_root)
        # Derive a job slug from the manifest content itself
        try:
            m = load_manifest(str(manifest_path))
            job_slug = m.job_id
        except Exception:
            job_slug = manifest_path.stem
    else:
        print("Usage: python examples/run_fake_job.py [manifest_path]", file=sys.stderr)
        sys.exit(2)

    output_dir = _repo_root / "examples" / "out" / job_slug

    print("=" * 52)
    print("  Desktop AI Job Runtime Contracts — Fake Job Runner")
    print("=" * 52)
    print()
    print(f"  Manifest  : {manifest_path}")
    print(f"  Output    : {output_dir}")
    print()

    manifest = run_job(str(manifest_path), output_dir=str(output_dir))

    print(f"  job_id        : {manifest.job_id}")
    print(f"  job_type      : {manifest.job_type}")
    print(f"  status        : {manifest.status}")
    print(f"  artifact count: {len(manifest.artifacts)}")
    print(f"  result_manifest: {(output_dir / 'result_manifest.json').resolve()}")
    print(f"  execution_trace: {(output_dir / 'execution_trace.json').resolve()}")
    print()

    # Show trace events
    trace_path = output_dir / "execution_trace.json"
    if trace_path.exists():
        trace_data = json.loads(trace_path.read_text(encoding="utf-8"))
        print("  Trace events:")
        for ev in trace_data.get("events", []):
            print(f"    [{ev['stage']}] {ev['message']}")

    print()
    print("  Done.")


if __name__ == "__main__":
    main()