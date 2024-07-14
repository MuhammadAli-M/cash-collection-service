from django.test import TestCase

from domains.collection.infra.models.task import Task
from domains.collection.infra.repos.tasks_dao import TasksDao
from tests.collection.common.datetime_helper import get_datetime_after_week
from tests.collection.infra.repos.fixtures import (
    create_collector,
    create_customer,
    create_user,
)


class TasksDaoTest(TestCase):

    def test_get_tasks_works(self):
        # arrange
        user1 = create_user(suffix="1")
        collector1 = create_collector(user=user1)
        task1_c1 = Task.objects.create(
            collector_id=collector1.id,
            is_collected=True,
            amount_due=50,
            amount_due_at=get_datetime_after_week(),
            customer=create_customer(),
        )
        task2_c1 = Task.objects.create(
            collector_id=collector1.id,
            is_collected=False,
            amount_due=50,
            amount_due_at=get_datetime_after_week(),
            customer=create_customer(),
        )

        collector2 = create_collector(user=create_user(suffix="2"))
        task1_c2 = Task.objects.create(
            collector_id=collector2.id,
            is_collected=True,
            amount_due=50,
            amount_due_at=get_datetime_after_week(),
            customer=create_customer(),
        )
        task2_c2 = Task.objects.create(
            collector_id=collector2.id,
            is_collected=False,
            amount_due=50,
            amount_due_at=get_datetime_after_week(),
            customer=create_customer(),
        )

        # act
        tasks = TasksDao().get_tasks(user_id=user1.id, is_collected=False)

        # assert
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], task2_c1)

    def test_get_task_works(self):
        # arrange
        user1 = create_user(suffix="1")
        collector1 = create_collector(user=user1)
        task1_c1 = Task.objects.create(
            collector_id=collector1.id,
            is_collected=True,
            amount_due=50,
            amount_due_at=get_datetime_after_week(),
            customer=create_customer(),
        )
        task2_c1 = Task.objects.create(
            collector_id=collector1.id,
            is_collected=False,
            amount_due=50,
            amount_due_at=get_datetime_after_week(),
            customer=create_customer(),
        )

        # act
        task = TasksDao().get_task(id=task1_c1.id)

        # assert
        self.assertEqual(task, task1_c1)
