import unittest
from lab7 import boyer_moore_search

class TestBoyerMooreSearch(unittest.TestCase):

    def test_single_match(self):
        self.assertEqual(boyer_moore_search("abcdefg", "cde"), [2])

    def test_no_match(self):
        self.assertEqual(boyer_moore_search("abcdefg", "xyz"), [])

    def test_empty_needle(self):
        self.assertEqual(boyer_moore_search("abcdef", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(boyer_moore_search("", "abc"), [])

    def test_both_empty(self):
        self.assertEqual(boyer_moore_search("", ""), [])

unittest.main()