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

    def test_is_freeze_safe_true_for_frozen_inactive(self):
        frozen_inactive_status = create_status(is_frozen=True, is_active=False)

        self.assertTrue(frozen_inactive_status.is_freeze_safe())

    def test_is_freeze_safe_true_for_unfrozen_active(self):
        unfrozen_active_status = create_status(is_frozen=False, is_active=True)

        self.assertTrue(unfrozen_active_status.is_freeze_safe())

    def test_is_freeze_safe_false_frozen_active(self):
        frozen_active_status = create_status(is_frozen=True, is_active=True)

        self.assertFalse(frozen_active_status.is_freeze_safe())
