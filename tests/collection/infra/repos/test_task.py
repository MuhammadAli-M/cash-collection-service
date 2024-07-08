from django.test import TestCase

from domains.collection.infra.models.task import Task
from tests.collection.infra.repos.fixtures import create_collector


class TaskTest(TestCase):

    def test_create_works(self):
        collector = create_collector()
        task = Task.objects.create(
            collector=collector,
        )
        self.assertIsNotNone(task.id)
        self.assertEqual(task.is_collected, False)
        self.assertIsNotNone(task.collector.id, collector.id)
        self.assertIsNotNone(collector.created_at)
        self.assertIsNotNone(collector.updated_at)
