from domains.collection.infra.models.collector import Collector
from domains.collection.infra.models.customer import Customer
from domains.collection.infra.models.task import Task
from domains.collection.infra.models.user import User
from tests.collection.common.datetime_helper import get_datetime_after_week


def create_task(collector=None, customer=None, is_collected=False):
    if collector is None:
        collector = create_collector()
    if customer is None:
        customer = create_customer()
    return Task.objects.create(
        amount_due=50,
        amount_due_at=get_datetime_after_week(),
        collector_id=collector.id,
        customer_id=customer.id,
        is_collected=is_collected,
    )


def create_customer() -> Customer:
    return Customer.objects.create(
        name="M",
        address="A",
    )


def create_collector(user=None):
    if user is None:
        user = create_user()
    return Collector.objects.create(amount=0, user_id=user.id)


def create_user(suffix=""):
    return User.objects.create_user(
        first_name="M", last_name="A", email=f"ma{suffix}@g.com", password="12345"
    )
