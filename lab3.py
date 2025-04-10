class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

def sum_of_depths(root: TreeNode) -> int:
    def prefix(node, depth):
        if node is None:
            return 0
        return depth + prefix(node.left, depth + 1) + prefix(node.right, depth + 1)
    return prefix(root, 0)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sum_of_depths(root)
print(sum_of_depths(root))