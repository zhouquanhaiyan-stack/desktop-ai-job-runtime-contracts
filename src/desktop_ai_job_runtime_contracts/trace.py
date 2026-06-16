# Desktop AI Job Runtime Contracts — trace.py
#
# Execution trace data structures for recording event-level
# progress during a job run.

from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class TraceEvent:
    event_id: str
    timestamp: str
    stage: str
    message: str
    metadata: Dict[str, str] = field(default_factory=dict)
    event_type: str = "GENERIC"


@dataclass
class ExecutionTrace:
    job_id: str
    events: List[TraceEvent] = field(default_factory=list)

    def add_event(
        self,
        stage: str,
        message: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> TraceEvent:
        event = TraceEvent(
            event_id=uuid.uuid4().hex[:12],
            timestamp=datetime.now(timezone.utc).isoformat(),
            stage=stage,
            message=message,
            metadata=metadata or {},
        )
        self.events.append(event)
        return event

    def to_dict(self) -> Dict[str, Any]:
        def _serialize(obj: Any) -> Any:
            if isinstance(obj, TraceEvent):
                return asdict(obj)
            return obj

        return {
            "job_id": self.job_id,
            "events": [_serialize(e) for e in self.events],
        }

    def save_trace(self, path: str | Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(self.to_dict(), indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ExecutionTrace":
        events = [
            TraceEvent(**e) for e in data.get("events", [])
        ]
        return cls(job_id=data["job_id"], events=events)
