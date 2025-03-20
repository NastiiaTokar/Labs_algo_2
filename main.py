import unittest
from lab2 import min_time_to_paint

class TestPainter(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(min_time_to_paint(10, 5, [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]), 100)

    def test_1_painter(self):
        self.assertEqual(min_time_to_paint(1, 2, [5, 10, 15]), (5 + 10 + 15) * 2)

    def test_more_painters_than_boards(self):
        self.assertEqual(min_time_to_paint(5, 3, [4, 7, 2]), 75)

    def test_large_case(self):
        self.assertEqual(min_time_to_paint(3, 1, [10, 20, 30, 40, 50]), 60)

unittest.main()