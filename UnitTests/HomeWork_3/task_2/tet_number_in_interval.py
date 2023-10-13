import unittest

from number_in_interval import number_in_interval


class TestNumberInInterval(unittest.TestCase):
    def test_number_more_then_100(self):
        self.assertFalse(number_in_interval(101))

    def test_number_less_then_25(self):
        self.assertFalse(number_in_interval(24))

    def test_number_is_25(self):
        self.assertFalse(number_in_interval(25))

    def test_number_is_100(self):
        self.assertFalse(number_in_interval(100))

    def test_number_in_interval(self):
        self.assertTrue(number_in_interval(56))