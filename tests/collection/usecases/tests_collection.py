from unittest import TestCase
from unittest.mock import MagicMock, Mock

from domains.collection.infra.repos.collectors_repo import CollectorsRepo
from domains.collection.infra.repos.tasks_repo import TasksRepo
from domains.collection.usecases.collection import (
    Collection,
    CollectionRequest, )
from domains.collection.usecases.exceptions import CollectorNotFound, \
    FrozenCollector, TaskNotFound
from tests.collection.entities import fixtures


class CollectionTests(TestCase):

    def test_execute_raises_if_collector_not_found(self):
        # arrange
        request = CollectionRequest(user_id=1, task_id=2)
        collectors_repo_mock = Mock(spec=CollectorsRepo)
        collectors_repo_mock.get_collector_by_user_id = MagicMock(
            return_value=None)
        # act + assert
        use_case = Collection(collectors_repo=collectors_repo_mock)

        with self.assertRaises(CollectorNotFound) as err:
            use_case.execute(request)

            self.assertEqual(err.exception.user_id,1)

    def test_execute_raises_if_collector_is_frozen(self):
        # arrange
        request = CollectionRequest(user_id=1, task_id=2)
        collectors_repo_mock = Mock(spec=CollectorsRepo)
        collector = fixtures.create_collector()
        collectors_repo_mock.get_collector_by_user_id = MagicMock(
            return_value=collector)

        frozen_status = fixtures.make_a_frozen_status(collector.id)
        collectors_repo_mock.get_latest_status = MagicMock(
            return_value=frozen_status)

        # act + assert
        use_case = Collection(collectors_repo=collectors_repo_mock)

        with self.assertRaises(FrozenCollector) as err:
            use_case.execute(request)

        self.assertEqual(err.exception.collector_id, collector.id)

    def test_execute_raises_if_task_not_existing(self):
        # arrange
        request = CollectionRequest(user_id=1, task_id=2)
        collectors_repo_mock = Mock(spec=CollectorsRepo)
        collector = fixtures.create_collector()
        collectors_repo_mock.get_collector_by_user_id = MagicMock(
            return_value=collector)

        not_frozen_status = fixtures.make_a_not_frozen_status(collector.id)
        collectors_repo_mock.get_latest_status = MagicMock(
            return_value=not_frozen_status)

        tasks_repo_mock = Mock(spec=TasksRepo)
        tasks_repo_mock.get_task = MagicMock(return_value=None)

        # act + assert
        use_case = Collection(collectors_repo=collectors_repo_mock,
                              tasks_repo=tasks_repo_mock)

        with self.assertRaises(TaskNotFound) as err:
            use_case.execute(request)

        self.assertEqual(err.exception.task_id, 2)
