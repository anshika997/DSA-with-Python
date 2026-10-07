class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):

        if root is None:
            return 0

        # Leaf node
        if root.left is None and root.right is None:
            return 1

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        # Only right child exists
        if root.left is None:
            return 1 + right

        # Only left child exists
        if root.right is None:
            return 1 + left

        # Both children exist
        return 1 + min(left, right)


# Creating the tree
#
#        3
#       / \
#      9   20
#         /  \
#        15   7

root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


# Calling the solution
solution = Solution()
result = solution.minDepth(root)


# Printing the answer
print("Minimum Depth:", result)