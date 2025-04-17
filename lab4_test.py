import unittest
from binary_tree_priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.q = PriorityQueue()
        self.q.insert("A", 1)
        self.q.insert("B", 5)
        self.q.insert("C", 10)

    def test_peek(self):
        self.assertEqual(self.q.peek(), "C")

    def test_pop(self):
        self.assertEqual(self.q.pop(), "C")
        self.assertEqual(self.q.pop(), "B")
        self.assertEqual(self.q.pop(), "A")
        self.assertIsNone(self.q.pop())

    def test_view(self):
        expected = [("C", 10), ("B", 5), ("A", 1)] 
        self.assertEqual(self.q.view(), expected)

unittest.main()