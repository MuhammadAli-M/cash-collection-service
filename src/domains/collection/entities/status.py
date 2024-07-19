from datetime import datetime, timedelta

from django.conf import settings

from domains.collection.entities.task import BaseEntity, CollectorID


class Status(BaseEntity):
    collector_id: CollectorID
    due_at: datetime
    is_frozen: bool
    is_active: bool

    def is_frozen_due(self) -> bool:
        is_due = datetime.now() > self.due_at
        return self.is_frozen and self.is_active and is_due

    def is_freeze_safe(self) -> bool:
        frozen_inactive = self.is_frozen and not self.is_active
        unfrozen_active = not self.is_frozen and self.is_active
        # it could be expressed as is_frozen XOR is_active
        return frozen_inactive or unfrozen_active

    @staticmethod
    def make_future_freeze_status(collector_id):
        future_freeze_date = (datetime.now() +
                              timedelta(settings.FREEZE_TOLERANCE_IN_DAYS))
        return Status(collector_id=collector_id,
                      is_frozen=True,
                      is_active=True,
                      due_at=future_freeze_date)
