from tests.collection.common.datetime_helper import get_datetime_after_week
from domains.collection.entities.task import Task


def create_task(amount_due=50, amount_due_at=get_datetime_after_week(),
                collector_id=1, customer_id=5, is_collected=True):
    return Task(
        collector_id=collector_id,
        is_collected=is_collected,
        amount_due=amount_due,
        amount_due_at=amount_due_at,
        customer_id=customer_id
    )
