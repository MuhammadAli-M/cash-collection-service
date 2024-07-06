from django.test import TestCase


class SimpleClass:
    simple_property: int = 0


class SimpleTest(TestCase):

    def test_execute_works(self):
        c = SimpleClass()
        assert c.simple_property == 0
