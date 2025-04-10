import unittest
from lab3 import TreeNode, sum_of_depths


class TestSumOfDepths(unittest.TestCase):
    def test_example_tree(self):
        
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        self.assertEqual(sum_of_depths(root), 6)

unittest.main()