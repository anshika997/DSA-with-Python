class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):

        if root is None:
            return True

        def compare(left, right):

            if left is None and right is None:
                return True

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            return compare(left.left, right.right) and compare(left.right, right.left)

        return compare(root.left, root.right)


# Create Tree
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)


# Check
solution = Solution()

print(solution.isSymmetric(root))
