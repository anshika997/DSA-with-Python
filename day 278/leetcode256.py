class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root):
        total_tilt = 0

        def treeSum(root):
            nonlocal total_tilt

            if root is None:
                return 0

            left = treeSum(root.left)
            right = treeSum(root.right)

            total_tilt += abs(left - right)

            return root.val + left + right

        treeSum(root)
        return total_tilt


# Tree: [4, 2, 9, 3, 5]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(9)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)

sol = Solution()
print(sol.findTilt(root))