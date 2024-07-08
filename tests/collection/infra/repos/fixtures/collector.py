from domains.collection.infra.repos.collector import Collector
from tests.collection.infra.repos.fixtures.user import create_user


def create_collector(user=None):
    if user is None:
        user = create_user()
    return Collector.objects.create(
        amount=0,
        user_id=user.id
    )
