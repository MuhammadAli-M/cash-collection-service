from django.test import TestCase

from tests.collection.entities.fixtures import create_collector


class CollectorTests(TestCase):

    def test_increase_amount_works(self):
        collector = create_collector(amount=60)

        collector.increment_amount(30)

        self.assertEqual(collector.amount, 90)

    # TODO: In the following tests, we should mock the env var
    #  COLLECTION_FREEZE_AMOUNT as this tests correctness depend on its value.
    def test_does_amount_above_freeze_limit_works_if_above(self):
        collector = create_collector(amount=4500)

        collector.increment_amount(500)

        self.assertTrue(collector.does_amount_above_freeze_limit())

    def test_does_amount_above_freeze_limit_works_if_below(self):
        collector = create_collector(amount=4500)

        collector.increment_amount(499)

        self.assertFalse(collector.does_amount_above_freeze_limit())
