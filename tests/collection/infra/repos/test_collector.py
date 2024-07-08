from domains.collection.infra.models.collector import Collector

from django.test import TestCase
from tests.collection.infra.repos.fixtures import create_user


class CollectorTest(TestCase):

    def test_create_works(self):
        user = create_user()
        collector = Collector.objects.create(
            amount=0,
            user_id=user.id
        )
        self.assertIsNotNone(collector.id)
        self.assertEqual(collector.amount, 0)
        self.assertIsNotNone(collector.user_id)
        self.assertEqual(collector.user_id, user.id)
        self.assertIsNotNone(collector.created_at)
        self.assertIsNotNone(collector.updated_at)