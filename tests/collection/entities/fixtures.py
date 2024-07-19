from datetime import UTC, datetime, timedelta

from domains.collection.entities.collector import Collector
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


def create_collector(amount=0):
    return Collector(
        id=1,
        amount=amount,
        user_id=2
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
        udpated_at=updated_at,
    )


def make_a_frozen_status(collector_id):
    yesterday_time = datetime.now() - timedelta(days=1)
    return create_status(collector_id=collector_id,
                         is_frozen=True,
                         is_active=True,
                         due_at=yesterday_time)

def make_a_not_frozen_status(collector_id):
    return create_status(collector_id=collector_id,
                         is_frozen=False,
                         is_active=True,
                         due_at=datetime.now())
