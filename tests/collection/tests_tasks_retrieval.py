from unittest.mock import Mock, MagicMock

from django.test import TestCase

from domains.collection.entities.task import Task
from domains.collection.infra.repos.tasks_repo import TasksRepo
from domains.collection.infra.usecases.tasks_retrieval import TasksRetrieval, \
    TasksRetrievalRequest


class TasksRetrievalTests(TestCase):

    def test_execute_works(self):
        # arrange
        request = TasksRetrievalRequest(collector_id=1)
        repo_mock = Mock(spec=TasksRepo)
        tasks = [Task(collector_id=1), Task(collector_id=2)]
        repo_mock.get_tasks = MagicMock(
            return_value=tasks)

        # act
        response = TasksRetrieval(repo=repo_mock).execute(request)

        # assert
        self.assertEqual(response.tasks, tasks)
        repo_mock.get_tasks.assert_called_once_with(
            collector_id=1,
            is_collected=False
        )
