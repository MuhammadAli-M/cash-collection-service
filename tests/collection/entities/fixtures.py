from datetime import datetime, UTC

from domains.collection.entities.status import Status
from domains.collection.entities.task import Task
from tests.collection.common.datetime_helper import get_datetime_after_week


def create_task(
    amount_due=50,
    amount_due_at=get_datetime_after_week(),
    collector_id=1,
    customer_id=5,
    is_collected=True,
):
    return Task(
        collector_id=collector_id,
        is_collected=is_collected,
        amount_due=amount_due,
        amount_due_at=amount_due_at,
        customer_id=customer_id,
    )


def create_status(
        is_frozen: bool,
        is_active: bool,
        collector_id=1,
        due_at=get_datetime_after_week(),
        created_at=datetime.now(UTC),
        updated_at=datetime.now(UTC),
):
    return Status(
        is_frozen=is_frozen,
        is_active=is_active,
        collector_id=collector_id,
        due_at=due_at,
        created_at=created_at,
        udpated_at=updated_at
    )
