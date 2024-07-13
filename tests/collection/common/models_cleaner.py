from domains.collection.infra.models.collector import Collector
from domains.collection.infra.models.task import Task
from domains.collection.infra.models.user import User


def clear_tasks():
    Task.objects.all().delete()


def clear_users():
    Collector.objects.all().delete()
    User.objects.all().delete()
