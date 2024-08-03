from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import MagicMock, Mock

from domains.collection.infra.repos.collectors_repo import CollectorsRepo
from domains.collection.infra.repos.tasks_repo import TasksRepo
from domains.collection.usecases.collection import (
    Collection,
    CollectionRequest, )
from domains.collection.usecases.exceptions import CollectorNotFound, \
    FrozenCollector, TaskNotFound

from tests.collection.common.datetime_helper import get_datetime_yesterday, \
    is_datetime_close_to
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

            self.assertEqual(err.exception.user_id, 1)

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

    def test_execute_updates_task_and_collector(self):
        # arrange
        request = CollectionRequest(user_id=1, task_id=2)
        collectors_repo_mock = Mock(spec=CollectorsRepo)
        collector = fixtures.create_collector(amount=0)
        collectors_repo_mock.get_collector_by_user_id = MagicMock(
            return_value=collector)

        not_frozen_status = fixtures.make_a_not_frozen_status(collector.id)
        collectors_repo_mock.get_latest_status = MagicMock(
            return_value=not_frozen_status)

        tasks_repo_mock = Mock(spec=TasksRepo)
        not_collected_task = fixtures.create_task(
            collector_id=collector.id,
            amount_due=100,
            amount_due_at=get_datetime_yesterday(),
            is_collected=False
        )
        tasks_repo_mock.get_task = MagicMock(return_value=not_collected_task)

        # act
        use_case = Collection(collectors_repo=collectors_repo_mock,
                              tasks_repo=tasks_repo_mock)
        use_case.execute(request)

        # assert
        captured_collector = collectors_repo_mock.save_collector.call_args[0][0]
        self.assertEqual(captured_collector.amount, 100)

        captured_task = tasks_repo_mock.save_task.call_args[0][0]
        self.assertEqual(captured_task.is_collected, True)

        collectors_repo_mock.save_status.assert_not_called()

    def test_execute_add_future_freeze_status_if_collector_exceeds_threshold(
            self):
        # arrange
        request = CollectionRequest(user_id=1, task_id=2)
        collectors_repo_mock = Mock(spec=CollectorsRepo)
        collector = fixtures.create_collector(amount=4900)
        collectors_repo_mock.get_collector_by_user_id = MagicMock(
            return_value=collector)

        not_frozen_status = fixtures.make_a_not_frozen_status(collector.id)
        collectors_repo_mock.get_latest_status = MagicMock(
            return_value=not_frozen_status)

        tasks_repo_mock = Mock(spec=TasksRepo)
        not_collected_task = fixtures.create_task(
            collector_id=collector.id,
            amount_due=100,
            amount_due_at=get_datetime_yesterday(),
            is_collected=False
        )
        tasks_repo_mock.get_task = MagicMock(return_value=not_collected_task)

        # act
        use_case = Collection(collectors_repo=collectors_repo_mock,
                              tasks_repo=tasks_repo_mock)
        use_case.execute(request)

        # assert
        captured_collector = collectors_repo_mock.save_collector.call_args[0][0]
        self.assertEqual(captured_collector.amount, 5000)

        captured_task = tasks_repo_mock.save_task.call_args[0][0]
        self.assertEqual(captured_task.is_collected, True)

        collectors_repo_mock.save_status.assert_called_once()
        captured_status = collectors_repo_mock.save_status.call_args[0][0]
        self.assertEqual(captured_status.collector_id, collector.id)
        self.assertEqual(captured_status.is_frozen, True)
        self.assertEqual(captured_status.is_active, True)
        expected_due_at = datetime.now() + timedelta(days=2)
        self.assertTrue(
            is_datetime_close_to(captured_status.due_at, expected_due_at))
