# Adapter Contract

## Overview

The adapter boundary separates the generic job contract layer from framework-specific execution logic. Adapters implement the ``BaseRuntimeAdapter`` abstract class.

## BaseRuntimeAdapter

```python
class BaseRuntimeAdapter(ABC):

    @abstractmethod
    def get_info(self) -> RuntimeAdapterInfo:
        \"\"\"Return metadata about this adapter.\"\"\"

    @abstractmethod
    def run(self, manifest: JobManifest, trace: ExecutionTrace) -> JobManifest:
        \"\"\"Execute the job described by the manifest.

        The adapter mutates the manifest status, appends artifacts,
        and records execution events in the trace.

        Returns:
            The updated JobManifest with final status and artifacts.
        \"\"\"
```

## FakeRuntimeAdapter

The ``FakeRuntimeAdapter`` is a reference implementation included for testing and demonstration. It:

1. Sets ``manifest.status`` to ``RUNNING``
2. Records an ``adapter_started`` trace event
3. Scans inputs and records an ``input_scanned`` event
4. Creates a fake PREVIEW artifact (fake_preview.txt)
5. Creates a fake LOG artifact (fake_run.log)
6. Writes both placeholder files to the output directory
7. Records an ``artifact_created`` trace event
8. Sets ``manifest.status`` to ``SUCCEEDED``
9. Records an ``adapter_finished`` trace event

## Implementing a custom adapter

```python
from desktop_ai_job_runtime_contracts import (
    BaseRuntimeAdapter, RuntimeAdapterInfo, RuntimeCapability,
    JobManifest, ExecutionTrace,
)

class MyCustomAdapter(BaseRuntimeAdapter):

    def get_info(self) -> RuntimeAdapterInfo:
        return RuntimeAdapterInfo(
            adapter_id="my-adapter",
            name="My Custom Adapter",
            version="1.0.0",
            capabilities=[RuntimeCapability.LOCAL_EXECUTION],
        )

    def run(self, manifest: JobManifest, trace: ExecutionTrace) -> JobManifest:
        trace.add_event("custom_start", "Starting custom execution")
        # ... actual AI inference logic ...
        manifest.status = JobStatus.SUCCEEDED
        trace.add_event("custom_finish", "Custom execution finished")
        return manifest
```
