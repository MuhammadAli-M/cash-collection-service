from unittest import TestCase
from unittest.mock import MagicMock, Mock

from domains.collection.infra.repos.tasks_repo import TasksRepo
from domains.collection.usecases.tasks_retrieval import (
    TasksRetrieval,
    TasksRetrievalRequest,
)
from tests.collection.entities.fixtures import create_task


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
        repo_mock.get_tasks.assert_called_once_with(user_id=1, is_collected=True)
