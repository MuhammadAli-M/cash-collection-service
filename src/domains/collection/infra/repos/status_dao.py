from typing import Optional

from domains.collection.infra.models.status import Status


class StatusDao:
    def save_status(self, dbo: Status) -> Status:
        dbo.save()
        return dbo

    def get_latest(self, collector_id: int) -> Optional[Status]:
        return (
            Status.objects.filter(collector_id=collector_id)
            .order_by("-created_at")[0:1]
        ).first()
