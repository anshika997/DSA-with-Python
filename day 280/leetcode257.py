
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        result = 0

        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                result += root.left.val

        left = self.sumOfLeftLeaves(root.left)
        right = self.sumOfLeftLeaves(root.right)

        return result + left + right


# Create the sample tree:
#        3
#       / \
#      9   20
#         /  \
#        15   7

root = TreeNode(
    3,
    TreeNode(9),
    TreeNode(20, TreeNode(15), TreeNode(7))
)

solution = Solution()
answer = solution.sumOfLeftLeaves(root)

print("Sum of left leaves:", answer)
