from copy import copy

from django.test import TestCase

from domains.collection.infra.models.collector import Collector
from domains.collection.infra.repos.collector_dao import CollectorDao
from tests.collection.infra.repos.fixtures import create_user


class CollectorDaoTest(TestCase):

    def test_save_collector_works_if_not_existing(self):
        # arrange
        user = create_user()
        collector = Collector(user_id=user.id, amount=20)

        # act
        dao = CollectorDao()
        saved = dao.save_collector(collector)

        # assert
        self.assertIsNotNone(saved.id)
        self.assertEqual(saved.user, collector.user)
        self.assertEqual(saved.amount, collector.amount)
        self.assertEqual(saved.created_at, collector.created_at)
        self.assertEqual(saved.updated_at, collector.updated_at)

    def test_save_collector_works_if_existing(self):
        # arrange
        user = create_user()
        collector = Collector(user_id=user.id, amount=20)
        dao = CollectorDao()
        saved = dao.save_collector(collector)

        # act
        saved_copy = copy(saved)
        saved_copy.amount += 30
        saved_again = dao.save_collector(saved_copy)

        # assert
        self.assertIsNotNone(saved_again.id)
        self.assertEqual(saved_again.user, saved.user)
        self.assertEqual(saved_again.amount, saved.amount + 30)
        self.assertEqual(saved_again.created_at, saved.created_at)
        self.assertNotEqual(saved_again.updated_at, saved.updated_at)
