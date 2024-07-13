from typing import Optional

from domains.collection.entities.status import Status
from domains.collection.infra.models.status import Status as StatusDbo


class StatusConverter:

    def to_domain(self, dbo: Optional[StatusDbo]) -> Optional[Status]:
        """
        Convert to domain entity
        """

        if dbo is None:
            return None

        return Status(
            id=dbo.id,
            collector_id=dbo.collector.id,
            due_at=dbo.due_at,
            is_frozen=dbo.is_frozen,
            is_active=dbo.is_active,
            created_at=dbo.created_at,
            updated_at=dbo.updated_at,
        )

    def to_dbo(self, domain: Status) -> StatusDbo:
        """
        Convert to dbo(database object)
        """
        return StatusDbo(
            collector_id=domain.collector_id,
            due_at=domain.due_at,
            is_frozen=domain.is_frozen,
            is_active=domain.is_active,
            created_at=domain.created_at,
            updated_at=domain.updated_at,
        )
