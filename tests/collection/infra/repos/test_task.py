from django.test import TestCase

from domains.collection.infra.models.task import Task
from tests.collection.common.datetime_helper import get_datetime_after_week
from tests.collection.infra.repos.fixtures import create_collector, create_customer


class TaskTest(TestCase):

    def test_create_works(self):
        collector = create_collector()
        customer = create_customer()
        some_datetime = get_datetime_after_week()
        task = Task.objects.create(
            amount_due=50,
            amount_due_at=some_datetime,
            collector=collector,
            customer=customer,
            is_collected=False,
        )
        self.assertIsNotNone(task.id)
        self.assertEqual(task.amount_due, 50)
        self.assertEqual(task.amount_due_at, some_datetime)
        self.assertEqual(task.customer.id, customer.id)
        self.assertEqual(task.is_collected, False)
        self.assertIsNotNone(task.collector.id, collector.id)
        self.assertIsNotNone(collector.created_at)
        self.assertIsNotNone(collector.updated_at)
