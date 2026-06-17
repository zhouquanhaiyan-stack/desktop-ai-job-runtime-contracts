# Deterministic Runtime Contract System (DRCS)

[![CI](https://github.com/zhouquanhaiyan-stack/desktop-ai-job-runtime-contracts/actions/workflows/ci.yml/badge.svg)](https://github.com/zhouquanhaiyan-stack/desktop-ai-job-runtime-contracts/actions/workflows/ci.yml)



A structured execution system that transforms job specifications into deterministic execution graphs with event-sourced traceability and isolated runtime adapters.

## Key Idea

This system separates:

- Specification (what to run)
- Execution Graph (how to run)
- Adapter (runtime behavior)
- Trace (what happened)
- Artifacts (outputs)

## Architecture Overview

```text
Contract Spec
     |
     v
Execution Graph
     |
     v
Runtime Adapter
     |
     v
Event Trace
     |
     v
Artifacts
```

## Computational Model

This system defines a contract-driven deterministic execution model (CEM), where computation is expressed as structured contracts evaluated through a fixed execution graph.

See [Contract Execution Model](docs/computational_model.md) and [Paradigm comparison](docs/paradigm_comparison.md).

## System Invariants

- I1: Determinism invariant
- I2: Graph invariance (structure fixed)
- I3: Trace immutability
- I4: Adapter isolation
- I5: Artifact consistency

See [System invariants](docs/invariants.md).

## Overview

**desktop-ai-job-runtime-contracts** is a lightweight, dependency-free Python library that defines the contract surface for running AI inference jobs in a local desktop environment. It provides job manifest schemas, a runtime adapter boundary, execution tracing, and an export guard stub — all without any external dependencies.

This project is maintained as a small, practical contract layer for local desktop AI workflow experiments and tooling.

## Why this exists

Desktop AI tools often share common patterns — job submission, status tracking, output artifact management, and execution tracing — but each tool reimplements them in a slightly different way. This library captures those shared patterns as reusable typed contracts so that adapter authors and tool builders can focus on the actual AI work rather than plumbing.

## Features

- **Job manifests**: structured JSON schema for job inputs, outputs, and metadata
- **Runtime adapters**: abstract base class + a FakeRuntimeAdapter for testing and demos
- **Execution traces**: event-level logging of job progress with timestamps
- **Export guard**: sample policy enforcement for artifact-level access control
- **Zero dependencies**: pure Python, standard library only
- **Fully tested**: comprehensive unit test suite

## Quick start

`ash
# Clone the repository
git clone https://github.com/zhouquanhaiyan-stack/desktop-ai-job-runtime-contracts.git
cd desktop-ai-job-runtime-contracts

# Run the example job (no install required)
python examples/run_fake_job.py

# Run the test suite
python -m unittest discover -s tests
`

## Examples

This repository includes three manifest examples demonstrating the contract
across different job types. Each can be run through the same runner:

```bash
# Audio (default)
python examples/run_fake_job.py

# Image
python examples/run_fake_job.py examples/fake_image_job.json

# Text
python examples/run_fake_job.py examples/fake_text_job.json
```

See [examples documentation](docs/examples.md) for detailed descriptions.

## Example job manifest

`json
{
  \"job_id\": \"fake-audio-job-001\",
  \"job_type\": \"audio\",
  \"inputs\": [
    {
      \"input_id\": \"in-001\",
      \"path\": \"samples/input.wav\",
      \"media_type\": \"audio/wav\"
    }
  ],
  \"output_dir\": \"examples/out/fake-audio-job-001\",
  \"status\": \"pending\",
  \"artifacts\": []
}
`

## Runtime adapter boundary

Adapters implement BaseRuntimeAdapter and translate the generic job manifest into framework-specific execution. The included FakeRuntimeAdapter demonstrates the lifecycle:

1. Load and validate manifest
2. Update status to RUNNING
3. Scan inputs and record trace events
4. Produce artifacts (preview, log, etc.)
5. Update status to SUCCEEDED
6. Persist result manifest and execution trace

## Execution trace

Every job run produces an ordered list of TraceEvent entries, each with a unique ID, UTC timestamp, stage name, message, and optional metadata. This gives downstream tooling a lightweight audit trail of what happened during execution.

## Architecture v2 (Stable)

- Deterministic execution graph (scan -> execute -> finalize)
- Static contract specification layer
- Event-sourced trace model
- Fake adapter runtime isolation

See [Architecture v2 stable documentation](docs/architecture_v2_stable.md).

## Architecture v3 (Formal Spec Layer)

- Declarative runtime specification
- Schema-driven contract definitions
- Formal execution model representation
- Audit-ready system structure

See [Architecture v3](docs/architecture_v3.md) and [Specification overview](docs/specification_overview.md).

## Export guard policy

The ExportGuard is a **demonstration-only** stub that maps artifact kinds to plan tiers:

| Plan     | Allowed artifacts                |
| -------- | -------------------------------- |
| ree   | preview                          |
| plus   | preview, export (limited)        |
| pro    | all artifact kinds               |
| unknown  | blocked                          |

This is not a real licensing or authorization system. It exists purely to illustrate where an export policy boundary could be inserted in a job runtime pipeline.

## Project structure

`
desktop-ai-job-runtime-contracts/
  README.md
  LICENSE
  pyproject.toml
  .gitignore
  CHANGELOG.md
  CONTRIBUTING.md
  SECURITY.md
  docs/
    architecture.md
    job_manifest.md
    adapter_contract.md
    execution_trace.md
    export_guard.md
  src/
    desktop_ai_job_runtime_contracts/
      __init__.py
      contracts.py
      manifest.py
      adapter.py
      trace.py
      export_guard.py
      runner.py
  examples/
    fake_audio_job.json
    fake_image_job.json
    fake_text_job.json
    run_fake_job.py
  tests/
    test_manifest.py
    test_adapter.py
    test_trace.py
    test_export_guard.py
`

The project uses a small CI workflow to verify syntax, unit tests, and the example runner across supported Python versions.

## Roadmap

Maintenance roadmap: [docs/maintenance_roadmap.md](docs/maintenance_roadmap.md)

- [ ] Additional runtime adapter examples (e.g., ONNX, llama.cpp)
- [ ] Streaming trace support for long-running jobs
- [ ] Artifact hashing and integrity verification
- [ ] Plugin-style adapter discovery


The project uses a small CI workflow to verify syntax, unit tests, and the example runner across supported Python versions.


## Release

Current release: v0.1.0

Release notes: [docs/releases/v0.1.0.md](docs/releases/v0.1.0.md)
## Maintainer note

This project is maintained as an open-source reference implementation for local desktop AI workflow contracts. It is not a product, and no real licensing, payment, or server-side infrastructure is included. Contributions and feedback are welcome.

See the [Maintainer Workflow](docs/maintainer_workflow.md) for the change process.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Security

See [SECURITY.md](SECURITY.md) for reporting vulnerabilities.

## License

MIT — see [LICENSE](LICENSE) for the full text.

## System Overview (v4)

This repository represents a deterministic runtime contract system designed for reproducible execution, structured observability, and strict boundary isolation between contract definition and runtime execution.

See [System overview v4](docs/system_overview_v4.md) and [Architecture diagram v4](docs/architecture_diagram_v4.md).




