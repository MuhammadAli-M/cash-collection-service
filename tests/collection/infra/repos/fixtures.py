from domains.collection.infra.models.collector import Collector
from domains.collection.infra.models.task import Task
from domains.collection.infra.models.user import User


def create_task(collector=None):
    if collector is None:
        collector = create_collector()
    return Task.objects.create(
        collector_id=collector.id
    )


def create_collector(user=None):
    if user is None:
        user = create_user()
    return Collector.objects.create(
        amount=0,
        user_id=user.id
    )


def create_user():
    return User.objects.create_user(
        first_name="M",
        last_name="A",
        email="ma@g.com",
        password="12345"
    )