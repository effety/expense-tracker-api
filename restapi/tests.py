# from django.test import TestCase
from unittest import TestCase

# Create your tests here.
def two_integers_sum(a, b):
    return a + b


def two_multi_sum(a, b):
    return a * b


class TestSum(TestCase):
    def test_sum(self):
        self.assertEqual(two_integers_sum(1, 2), 3)

    def test_m(self):
        self.assertEqual(two_multi_sum(2, 2), 4)
