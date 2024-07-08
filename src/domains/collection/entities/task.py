from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

CollectorID = int


class BaseEntity(BaseModel):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Task(BaseEntity):
    collector_id: CollectorID
    is_collected: bool = False
