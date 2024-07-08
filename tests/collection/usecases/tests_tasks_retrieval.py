from unittest.mock import Mock, MagicMock

from unittest import TestCase

from tests.collection.entities.fixtures import create_task
from domains.collection.entities.task import Task
from domains.collection.infra.repos.tasks_repo import TasksRepo
from domains.collection.infra.usecases.tasks_retrieval import TasksRetrieval, \
    TasksRetrievalRequest


class TasksRetrievalTests(TestCase):

    def test_execute_works(self):
        # arrange
        request = TasksRetrievalRequest(user_id=1)
        repo_mock = Mock(spec=TasksRepo)
        tasks = [create_task(), create_task()]
        repo_mock.get_tasks = MagicMock(return_value=tasks)

        # act
        response = TasksRetrieval(repo=repo_mock).execute(request)

        # assert
        self.assertEqual(response.tasks, tasks)
        repo_mock.get_tasks.assert_called_once_with(
            user_id=1,
            is_collected=True
        )
