class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum):

        if root is None:
            return False

        targetSum = targetSum - root.val

        # Leaf node
        if root.left is None and root.right is None:
            return targetSum == 0

        return (
            self.hasPathSum(root.left, targetSum)
            or
            self.hasPathSum(root.right, targetSum)
        )


# Create Tree
root = TreeNode(5)

root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)

root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)


# Target Sum
targetSum = 22

solution = Solution()

print(solution.hasPathSum(root, targetSum))