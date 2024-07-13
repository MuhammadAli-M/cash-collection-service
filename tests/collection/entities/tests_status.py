from datetime import datetime, timedelta

from django.test import TestCase

from tests.collection.entities.fixtures import create_status


class StatusTests(TestCase):

    def test_is_frozen_due_is_true_if_frozen_and_due_at_is_already_passed(self):
        status = create_status(
            is_frozen=True, is_active=True, due_at=datetime.now() - timedelta(seconds=1)
        )

        self.assertEqual(status.is_frozen_due(), True)

    def test_is_frozen_due_is_false_if_not_active(self):
        status = create_status(
            is_frozen=True,
            is_active=False,
            due_at=datetime.now() - timedelta(seconds=1),
        )

        self.assertEqual(status.is_frozen_due(), False)

    def test_is_frozen_due_is_false_if_not_frozen(self):
        status = create_status(
            is_frozen=False,
            is_active=True,
            due_at=datetime.now() - timedelta(seconds=1),
        )

        self.assertEqual(status.is_frozen_due(), False)

    def test_is_frozen_due_is_false_if_due_at_is_not_passed(self):
        status = create_status(
            is_frozen=True, is_active=True, due_at=datetime.now() + timedelta(seconds=1)
        )

        self.assertEqual(status.is_frozen_due(), False)
