from datetime import datetime
from typing import Optional

from domains.collection.entities.task import BaseEntity, CollectorID


class Status(BaseEntity):
    collector_id: CollectorID
    due_at: datetime
    is_frozen: bool
    is_active: bool


    def is_frozen_due(self) -> bool:
        is_due = datetime.now() > self.due_at
        return self.is_frozen and self.is_active and is_due
