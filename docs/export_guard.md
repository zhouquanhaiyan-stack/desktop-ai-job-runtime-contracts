# Export Guard

## Overview

The ExportGuard is a **demonstration-only** stub that illustrates how an export policy boundary could work in a job runtime pipeline. It does **not** contain any real licensing, payment, authorization, or server-side logic.

## Plan tiers

The guard defines three sample plan tiers:

| Plan   | Description                                                   |
|--------|---------------------------------------------------------------|
| ree | Preview-only access. Export and other artifact kinds blocked. |
| plus | Preview and limited export allowed.                           |
| pro  | All artifact kinds allowed.                                   |

Unknown plan names are rejected with a clear error reason.

## How it works

`python
from desktop_ai_job_runtime_contracts import ArtifactKind, ExportGuard

guard = ExportGuard(plan_name=\"free\")

# Check if a specific artifact kind is allowed
decision = guard.evaluate(plan_name=\"plus\", artifact_kind=ArtifactKind.EXPORT)
print(decision.allowed)   # True
print(decision.reason)    # \"Plan 'plus' allows limited export for export artifacts.\"
`

## ExportDecision

| Field          | Type          | Description                           |
|----------------|---------------|---------------------------------------|
| llowed      | ool        | Whether the artifact kind is permitted|
| eason       | str         | Human-readable explanation            |
| plan_name    | str         | The plan name used for evaluation     |
| rtifact_kind| ArtifactKind| The artifact kind checked             |

## Important note

**This is not a real authorization system.** The plan tiers, policies, and evaluation logic are examples only. A real-world export guard would integrate with an authentication service, license manager, or payment provider. This stub exists to demonstrate:

1. Where an export policy boundary fits in the job runtime architecture
2. How policy decisions can be modeled as typed data structures
3. A testable pattern for artifact-level access control
