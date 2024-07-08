from dataclasses import dataclass
from datetime import datetime
from typing import Optional

CollectorID = int


class BaseEntity:
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class Task(BaseEntity):
    collector_id: CollectorID
    is_collected: bool = False
