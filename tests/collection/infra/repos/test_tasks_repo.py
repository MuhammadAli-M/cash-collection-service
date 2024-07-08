from datetime import datetime

from django.test import TestCase

from domains.collection.entities.task import Task
from domains.collection.infra.repos.tasks_repo import TasksRepo
from tests.collection.infra.repos.fixtures import create_collector


class TasksRepoTest(TestCase):

    def test_save_task_works(self):
        collector = create_collector()

        task = Task(collector_id=collector.id, is_collected=True)

        repo = TasksRepo()
        saved_task = repo.save_task(task)

        self.assertIsNotNone(saved_task.id)
        self.assertEqual(saved_task.is_collected, True)
        self.assertEqual(saved_task.collector_id, collector.id)
