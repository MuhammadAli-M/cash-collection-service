from datetime import datetime, timedelta

from django.test import TestCase

from tests.collection.entities.fixtures import create_status, create_task


class TaskTests(TestCase):

    def test_set_collected_true_if_collected_is_false(self):
        task = create_task(is_collected=False)
        task.set_collected()

        self.assertTrue(task.is_collected)