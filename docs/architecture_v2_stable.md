# Architecture v2 (Stable)

## Overview

Architecture v2 defines a deterministic runtime contract structure for local job execution. It separates the contract specification, execution graph, adapter boundary, trace events, and typed artifacts into clear layers.

```text
Contract Spec -> Execution Graph -> Adapter -> Trace -> Artifacts
```

## Deterministic Execution Graph

Every job manifest maps to the same three-stage graph:

```text
scan -> execute -> finalize
```

The graph has no dynamic branching. It exists to make the runtime flow easy to inspect, test, and document.

## Contract Spec Layer

The contract specification layer is a static schema holder. It lists supported job fields, artifact types, and trace event labels without performing validation or runtime execution.

## Event Sourcing Model

Execution traces are append-only event lists. Each trace event records an event identifier, timestamp, stage, message, metadata, and event type. Existing trace events keep the generic event type unless a caller provides a more specific label.

## Adapter Isolation Model

The runtime adapter layer remains isolated behind the existing adapter interface. The stable v2 architecture keeps the fake runtime as the only included adapter implementation.

## Artifact System

Artifacts remain typed outputs associated with a job manifest. The stable v2 contract identifies preview, log, trace, and manifest artifacts as the core typed artifact set.
