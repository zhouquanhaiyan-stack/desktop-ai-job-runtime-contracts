# Architecture v3 - Formal Spec Layer

## Overview

Architecture v3 adds a formal specification layer above the stable v2 runtime structure. The goal is to make the runtime contract explicitly defined, machine-readable, audit-friendly, and suitable for presentation without changing runtime behavior.

```text
Spec -> Contract -> Graph -> Adapter -> Trace -> Artifact
```

## Why formal specification layer exists

The formal specification layer gives the project a clear description of its contract surface. Instead of relying only on implementation details, v3 records the expected job manifest shape, execution graph model, trace event model, artifact model, and adapter boundary as named specification artifacts.

## Relationship to v2 stable architecture

The v2 stable architecture introduced a deterministic execution graph with the fixed lifecycle:

```text
scan -> execute -> finalize
```

The v3 layer does not replace that model. It documents and structures it as a formal runtime specification so that the same deterministic execution design can be inspected by tools, reviewers, and documentation consumers.

## Runtime contract decomposition

The runtime contract is decomposed into these layers:

- Contract spec: static definitions for job, graph, trace, artifact, and adapter models
- Execution graph: deterministic directed acyclic graph with no dynamic branching
- Adapter boundary: isolated runtime adapter surface
- Trace model: append-only event stream for execution observability
- Artifact model: typed outputs linked to job execution

## Schema definitions

The v3 schema file provides static JSON definitions for the job manifest, execution graph, trace event, and artifact shapes. These schemas are documentation-grade and machine-readable. They are intended to make the runtime design easier to audit without adding dependencies or changing execution code.

## Execution lifecycle

The lifecycle remains deterministic:

```text
job manifest -> scan -> execute -> finalize -> trace and artifacts
```

Trace events provide event-sourced traceability across the lifecycle. Artifact records provide typed output references. The adapter remains isolated behind the runtime boundary.

The result is schema-driven runtime design: the system can describe what it expects before any adapter performs work, while runtime behavior remains stable and compatible with the v2 architecture.
