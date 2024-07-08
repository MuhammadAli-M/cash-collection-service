from domains.collection.infra.repos.collector import Collector
from domains.collection.infra.repos.user import User

from django.test import TestCase


class CollectorTest(TestCase):

    def test_create_works(self):
        user = self.create_user()
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

    @staticmethod
    def create_user():
        return User.objects.create_user(
            first_name="M",
            last_name="A",
            email="ma@g.com",
            password="12345"
        )
