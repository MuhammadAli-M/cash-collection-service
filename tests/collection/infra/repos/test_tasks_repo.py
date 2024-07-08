from unittest.mock import MagicMock, Mock

from django.test import TestCase

from domains.collection.entities.task import Task
from domains.collection.infra.repos.tasks_dao import TasksDao
from domains.collection.infra.repos.tasks_repo import TasksRepo
from tests.collection.infra.repos.fixtures import create_collector


class TasksRepoTest(TestCase):

    def test_save_task_works(self):
        # arrange
        collector = create_collector()
        task = Task(collector_id=collector.id, is_collected=True)
        repo = TasksRepo()

        # act
        saved_task = repo.save_task(task)

        # assert
        self.assertIsNotNone(saved_task.id)
        self.assertEqual(saved_task.is_collected, True)
        self.assertEqual(saved_task.collector_id, collector.id)

    def test_get_tasks_works(self):
        # arrange
        collector = create_collector()
        task = Task(collector_id=collector.id, is_collected=True)
        dao_mock = Mock(spec=TasksDao)
        dao_mock.get_tasks = MagicMock(return_value=[task])
        repo = TasksRepo(dao=dao_mock)

        # act
        tasks = repo.get_tasks(collector_id=1, is_collected=False)

        # assert
        self.assertEqual(tasks, [task])
        dao_mock.get_tasks.assert_called_once_with(1, False)
