from unittest import TestCase
from unittest.mock import MagicMock, Mock

from domains.collection.entities.task import Task
from domains.collection.infra.repos.tasks_dao import TasksDao
from domains.collection.infra.repos.tasks_repo import TasksRepo


class TasksRepoTest(TestCase):

    def test_save_task_works(self):
        # arrange
        collector_id = 1
        task = Task(collector_id=collector_id, is_collected=True)
        dao_mock = Mock(spec=TasksDao)
        saved_task_mock = task.copy(update=dict(id=2))
        dao_mock.save_task = MagicMock(return_value=saved_task_mock)
        repo = TasksRepo(dao=dao_mock)

        # act
        saved_task = repo.save_task(task)

        # assert
        self.assertEqual(saved_task.id, saved_task_mock.id)
        dao_mock.save_task.assert_called_once()

        # 0 first argument of the function, 0 first argument of the tuple
        captured_task = dao_mock.save_task.call_args[0][0]
        self.assertEqual(captured_task.collector_id, task.collector_id)
        self.assertEqual(captured_task.is_collected, task.is_collected)

    def test_get_tasks_works(self):
        # arrange
        collector_id = 1
        task = Task(collector_id=collector_id, is_collected=True)
        dao_mock = Mock(spec=TasksDao)
        dao_mock.get_tasks = MagicMock(return_value=[task])
        repo = TasksRepo(dao=dao_mock)

        # act
        tasks = repo.get_tasks(user_id=1, is_collected=False)

        # assert
        self.assertEqual(tasks, [task])
        dao_mock.get_tasks.assert_called_once_with(1, False)
