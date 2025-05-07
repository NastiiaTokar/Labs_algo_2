import unittest
from lab5 import Graph

class TestGraphRoot(unittest.TestCase):

    def test_single_root(self):
        g = Graph(3)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        
        self.assertEqual(g.find_root(), 0)

    def test_multiple_roots(self):
        g = Graph(3)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)

        self.assertIn(g.find_root(), [0, 1, 2])

    def test_single_vertex_graph(self):
        g = Graph(1)

        self.assertEqual(g.find_root(), 0)

unittest.main()