# Architecture

This document describes the overall architecture of the desktop-ai-job-runtime-contracts library.

## Overview

`
  Job Manifest (JSON)
        |
        v
  validate_manifest()
        |
        v
  BaseRuntimeAdapter.run()
        |
        +---> ExecutionTrace.add_event()
        +---> JobArtifact creation
        |
        v
  save_manifest() + trace.save_trace()
        |
        v
  result_manifest.json, execution_trace.json
`

## Components

### 1. Contracts (contracts.py)

Defines the core enumerations and dataclasses shared across all modules:

- **Enums**: JobType, JobStatus, ArtifactKind, RuntimeCapability
- **Data types**: JobInput, JobArtifact, RuntimeAdapterInfo

These are the building blocks for every other module.

### 2. Manifest (manifest.py)

Handles job manifest creation, serialization, and validation:

- JobManifest dataclass with typed fields
- rom_dict / 	o_dict for JSON conversion
- load_manifest / save_manifest for file I/O
- alidate_manifest for field-level constraint checking

### 3. Adapter (dapter.py)

Defines the runtime adapter boundary:

- BaseRuntimeAdapter — abstract class with get_info() and un() methods
- FakeRuntimeAdapter — demo implementation that simulates job execution

### 4. Trace (	race.py)

Records execution events:

- TraceEvent — individual event with ID, timestamp, stage, message, metadata
- ExecutionTrace — ordered event list with dd_event(), 	o_dict(), save_trace()

### 5. Export Guard (export_guard.py)

Demonstration policy layer:

- ExportDecision — result of a policy evaluation
- ExportGuard — sample free/plus/pro plan enforcement

### 6. Runner (unner.py)

Orchestration entry point:

- un_job() — loads manifest, validates, runs adapter, persists results

## Data flow

1. A job manifest (JSON) is loaded from disk.
2. The manifest is validated structurally.
3. A runtime adapter is selected (e.g., FakeRuntimeAdapter).
4. The adapter executes the job, recording events in an ExecutionTrace.
5. The adapter updates the manifest status and appends artifacts.
6. The final manifest and trace are persisted as JSON files.

## Design principles

- **Zero dependencies** — standard library only
- **Typed contracts** — all data structures are fully typed
- **Separation of concerns** — manifest, adapter, trace, and guard are independent modules
- **Testability** — the FakeRuntimeAdapter enables testing without real AI infrastructure
