from unittest import TestCase
from unittest.mock import MagicMock, Mock

from domains.collection.infra.repos.collector_dao import CollectorDao
from domains.collection.infra.repos.collectors_repo import CollectorsRepo
from domains.collection.infra.repos.status_dao import StatusDao
from tests.collection.common.models_cleaner import clear_tasks, clear_users
from tests.collection.entities.fixtures import create_collector, create_status


class CollectorsRepoTest(TestCase):

    def setUp(self):
        clear_tasks()
        clear_users()

    def test_get_collector_works_if_existing(self):
        # arrange
        collector = create_collector()
        dao_mock = Mock(spec=CollectorDao)
        dao_mock.get_collector = MagicMock(return_value=collector)
        repo = CollectorsRepo(dao=dao_mock)

        # act
        retrieved = repo.get_collector(collector_id=collector.id)

        # assert
        self.assertEqual(retrieved.id, collector.id)
        self.assertEqual(retrieved.amount, collector.amount)
        self.assertEqual(retrieved.user_id, collector.user_id)
        self.assertEqual(retrieved.created_at, collector.created_at)
        self.assertEqual(retrieved.updated_at, collector.updated_at)
        dao_mock.get_collector.assert_called_once_with(collector_id=collector.id)

    def test_get_collector_works_if_not_existing(self):
        # arrange
        dao_mock = Mock(spec=CollectorDao)
        dao_mock.get_collector = MagicMock(return_value=None)
        repo = CollectorsRepo(dao=dao_mock)

        # act
        arbitrary_non_existing_id = 100
        retrieved = repo.get_collector(collector_id=arbitrary_non_existing_id)

        # assert
        self.assertEqual(retrieved, None)
        dao_mock.get_collector.assert_called_once_with(
            collector_id=arbitrary_non_existing_id)

    def test_get_collector_by_user_id_works_if_existing(self):
        # arrange
        collector = create_collector()
        dao_mock = Mock(spec=CollectorDao)
        dao_mock.get_collector_by_user_id = MagicMock(return_value=collector)
        repo = CollectorsRepo(dao=dao_mock)

        # act
        retrieved = repo.get_collector_by_user_id(user_id=collector.user_id)

        # assert
        self.assertEqual(retrieved.id, collector.id)
        self.assertEqual(retrieved.amount, collector.amount)
        self.assertEqual(retrieved.user_id, collector.user_id)
        self.assertEqual(retrieved.created_at, collector.created_at)
        self.assertEqual(retrieved.updated_at, collector.updated_at)
        dao_mock.get_collector_by_user_id.assert_called_once_with(
            user_id=collector.user_id)

    def test_get_collector_by_user_id_works_if_not_existing(self):
        # arrange
        dao_mock = Mock(spec=CollectorDao)
        dao_mock.get_collector_by_user_id = MagicMock(return_value=None)
        repo = CollectorsRepo(dao=dao_mock)
        arbitrary_non_existing_id = 100

        # act
        retrieved = repo.get_collector_by_user_id(user_id=arbitrary_non_existing_id)

        # assert
        self.assertEqual(retrieved, None)
        dao_mock.get_collector_by_user_id.assert_called_once_with(
            user_id=arbitrary_non_existing_id)


    def test_get_latest_status_works(self):
        # arrange
        collector = create_collector()
        status1 = create_status(is_frozen=True, is_active=False, collector_id=collector.id)
        status2 = create_status(is_frozen=True, is_active=False,  collector_id=collector.id)

        status_dao_mock = Mock(spec=StatusDao)
        status_dao_mock.get_latest = MagicMock(return_value=status2)
        repo = CollectorsRepo(status_dao=status_dao_mock)

        # act
        retrieved_status = repo.get_latest_status(collector_id=collector.id)

        # assert
        expected_status = status2
        self.assertEqual(retrieved_status.collector_id, collector.id)
        self.assertEqual(retrieved_status.due_at, expected_status.due_at)
        self.assertEqual(retrieved_status.is_frozen, expected_status.is_frozen)
        self.assertEqual(retrieved_status.is_active, expected_status.is_active)
        self.assertEqual(retrieved_status.created_at, expected_status.created_at)
        self.assertEqual(retrieved_status.updated_at, expected_status.updated_at)
        status_dao_mock.get_latest.assert_called_once_with(
            collector_id=collector.id
        )
