from django.test import TestCase

from domains.collection.infra.models.status import Status
from domains.collection.infra.repos.status_dao import StatusDao
from tests.collection.common.datetime_helper import get_datetime_after_week
from tests.collection.infra.repos.fixtures import create_collector, create_user


class StatusesDaoTest(TestCase):

    def test_get_latest_active_works(self):
        # arrange
        user1 = create_user(suffix="1")
        collector1 = create_collector(user=user1)
        status1_c1 = Status.objects.create(
            collector_id=collector1.id,
            due_at=get_datetime_after_week(),
            is_frozen=True,
            is_active=True,
        )
        status2_c1 = Status.objects.create(
            collector_id=collector1.id,
            due_at=get_datetime_after_week(),
            is_frozen=True,
            is_active=False,
        )

        status3_c1 = Status.objects.create(
            collector_id=collector1.id,
            due_at=get_datetime_after_week(),
            is_frozen=True,
            is_active=True,
        )

        collector2 = create_collector(user=create_user(suffix="2"))
        status1_c2 = Status.objects.create(
            collector_id=collector2.id,
            due_at=get_datetime_after_week(),
            is_frozen=True,
            is_active=True,
        )
        status2_c2 = Status.objects.create(
            collector_id=collector2.id,
            due_at=get_datetime_after_week(),
            is_frozen=True,
            is_active=False,
        )

        # act
        status = StatusDao().get_latest(collector_id=collector1.id)

        # assert
        self.assertEqual(status, status3_c1)
