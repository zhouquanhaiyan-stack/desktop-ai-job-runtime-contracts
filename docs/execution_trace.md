# Execution Trace

## Overview

Execution traces provide a lightweight audit trail of what happened during a job run. Each trace is an ordered list of events recorded by the runtime adapter.

## TraceEvent

| Field      | Type             | Description                             |
|------------|------------------|-----------------------------------------|
| event_id   | str              | Unique hexadecimal identifier (12 chars)|
| timestamp  | str              | UTC ISO 8601 timestamp                  |
| stage      | str              | Stage name (e.g., adapter_started)     |
| message    | str              | Human-readable description             |
| metadata   | dict[str, str]   | Optional structured key-value data      |

## ExecutionTrace

| Field    | Type               | Description                    |
|----------|--------------------|--------------------------------|
| job_id   | str                | Job this trace belongs to      |
| events   | list[TraceEvent]   | Ordered list of trace events   |

## Usage

```python
from desktop_ai_job_runtime_contracts import ExecutionTrace

trace = ExecutionTrace(job_id="my-job")
trace.add_event("init", "Job initialized")
trace.add_event("progress", "Processing input 1 of 5")
trace.add_event("complete", "Job finished")
trace.save_trace("/path/to/execution_trace.json")
```

## Example output

```json
{
  "job_id": "fake-audio-job-001",
  "events": [
    {
      "event_id": "a1b2c3d4e5f6",
      "timestamp": "2026-06-17T02:00:00.000000+00:00",
      "stage": "adapter_started",
      "message": "FakeRuntimeAdapter started execution.",
      "metadata": {}
    }
  ]
}
```

## Purpose

Traces serve as an execution record that can be inspected by tooling, logged for debugging, or aggregated for monitoring. They intentionally contain no sensitive data or proprietary execution details.
