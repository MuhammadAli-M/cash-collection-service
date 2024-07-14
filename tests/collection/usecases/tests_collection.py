from unittest import TestCase
from unittest.mock import MagicMock, Mock

from domains.collection.infra.repos.collectors_repo import CollectorsRepo
from domains.collection.usecases.collection import (
    Collection,
    CollectionRequest, )
from domains.collection.usecases.exceptions import CollectorNotFound


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

