from typing import Optional

from domains.collection.infra.models.status import Status


class StatusDao:
    def save_status(self, dbo: Status) -> Status:
        dbo.save()
        return dbo

    def get_latest(self, collector_id: int, is_frozen: bool, is_active: bool) -> \
            Optional[Status]:
        return (Status.objects
                .filter(collector_id=collector_id,
                        is_frozen=is_frozen,
                        is_active=is_active)
                .order_by("-created_at")
                ).first()
