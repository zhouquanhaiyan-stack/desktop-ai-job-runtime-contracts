# System Invariants

## I1: Determinism invariant

The same contract input maps to the same fixed execution graph and produces the same contract-level output structure.

## I2: Graph invariance (structure fixed)

The execution graph shape is fixed by design. It is acyclic and follows the stable scan, execute, finalize ordering.

## I3: Trace immutability

Trace records are append-only observations of execution. Existing events are not rewritten as later events occur.

## I4: Adapter isolation

Runtime behavior is isolated behind the adapter boundary. The contract, graph, trace, and artifact layers remain separate from adapter implementation details.

## I5: Artifact consistency

Artifacts are typed output state records associated with a job. Each artifact has a stable identity, kind, path, media type, and metadata surface.
