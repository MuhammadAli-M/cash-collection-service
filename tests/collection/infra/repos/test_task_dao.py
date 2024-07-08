from django.test import TestCase

from domains.collection.infra.models.task import Task
from domains.collection.infra.repos.tasks_dao import TaskDao
from tests.collection.infra.repos.fixtures import create_collector, create_user


class TasksDaoTest(TestCase):

    def test_get_tasks_works(self):
        # arrange
        collector1 = create_collector(user=create_user(suffix="1"))
        task1_c1 = Task.objects.create(collector_id=collector1.id, is_collected=True)
        task2_c1 = Task.objects.create(collector_id=collector1.id, is_collected=False)

        collector2 = create_collector(user=create_user(suffix="2"))
        task1_c2 = Task.objects.create(collector_id=collector2.id, is_collected=True)
        task2_c2 = Task.objects.create(collector_id=collector2.id, is_collected=False)

        # act
        tasks = TaskDao().get_tasks(collector_id=collector1.id,
                                    is_collected=False)

        # assert
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], task2_c1)
