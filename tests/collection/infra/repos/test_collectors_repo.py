from unittest import TestCase
from unittest.mock import MagicMock, Mock

from domains.collection.infra.repos.collectors_repo import CollectorsRepo
from domains.collection.infra.repos.status_dao import StatusDao
from tests.collection.common.models_cleaner import clear_tasks, clear_users
from tests.collection.infra.repos.fixtures import create_collector, create_status


class CollectorsRepoTest(TestCase):

    def setUp(self):
        clear_tasks()
        clear_users()

    def test_get_tasks_works(self):
        # arrange
        collector = create_collector()
        status1 = create_status(is_frozen=True, is_active=False, collector=collector)
        status2 = create_status(is_frozen=True, is_active=False, collector=collector)

        status_dao_mock = Mock(spec=StatusDao)
        status_dao_mock.get_latest = MagicMock(return_value=status2)
        repo = CollectorsRepo(status_dao=status_dao_mock)

        # act
        status = repo.get_latest_status(
            collector_id=collector.id, is_frozen=True, is_active=False
        )

        # assert
        expected_status = status2
        self.assertEqual(status.collector_id, collector.id)
        self.assertEqual(status.due_at, expected_status.due_at)
        self.assertEqual(status.is_frozen, expected_status.is_frozen)
        self.assertEqual(status.is_active, expected_status.is_active)
        self.assertEqual(status.created_at, expected_status.created_at)
        self.assertEqual(status.updated_at, expected_status.updated_at)
        status_dao_mock.get_latest.assert_called_once_with(
            collector_id=collector.id, is_frozen=True, is_active=False
        )
