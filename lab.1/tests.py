import unittest
from main import is_monotonic

class TestMonotonicArray(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_monotonic([1, 2, 3, 4, 5]))
    def test_2(self):
        self.assertTrue(is_monotonic([5, 4, 3, 2, 1]))
    def test_3(self):
        self.assertFalse(is_monotonic([1, 2, 2, 3, 2, 4]))
    def test_4(self):
        self.assertTrue(is_monotonic([1, 1, 1, 1, 1]))
    def test_5(self):
        self.assertTrue(is_monotonic([10]))
    def test_6(self):
        self.assertFalse(is_monotonic([1, 3, 2]))

unittest.main()