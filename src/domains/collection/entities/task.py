from datetime import datetime
from typing import Optional

from pydantic import BaseModel

CollectorID = int
CustomerID = int
Money = int


class BaseEntity(BaseModel):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Task(BaseEntity):
    amount_due: Money
    amount_due_at: datetime
    customer_id: CustomerID
    collector_id: CollectorID
    is_collected: bool = False

    def set_collected(self):
        self.is_collected = True
