# Paradigm Comparison

## Imperative execution

Imperative execution describes computation as ordered statements. Control flow is embedded directly in code, and observability depends on what the implementation chooses to expose.

The Contract Execution Model separates the execution description from the runtime implementation. The contract and graph make the expected execution shape explicit before adapter execution occurs.

## Pipeline systems

Pipeline systems organize work into sequential or branched processing stages. They are useful for production workflows, but their behavior can be tied to operational configuration, external services, or runtime scheduling.

This system is smaller and stricter: it is a contract-driven deterministic execution model with a fixed graph structure and no external runtime dependency.

## Actor model

The actor model describes computation as independent actors exchanging messages. It emphasizes concurrency, message passing, and isolated actor state.

The Contract Execution Model does not define concurrent actors. It defines a deterministic contract-to-graph-to-trace flow with adapter isolation rather than actor coordination.

## Event sourcing systems

Event sourcing systems treat event logs as the source of truth for state reconstruction. They often include domain event stores, replay semantics, and long-lived state evolution.

This system uses event-sourced traceability in a narrower sense: trace events record what happened during deterministic execution. The trace is audit evidence, while the contract and artifacts remain the primary runtime surfaces.

## Positioning

This repository defines a contract-driven deterministic execution model. Computation is expressed as a structured contract, evaluated through a fixed execution graph, executed through an isolated adapter, observed through an append-only trace, and represented by typed artifacts.
