# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root):
        self.maxi = float('-inf')

        def solve(node):
            if node is None :
                return 0 

            leftsum = solve(node.left)
            if leftsum<0:
                leftsum=0
            rightsum = solve(node.right)
            if rightsum<0:
                rightsum=0
            self.maxi = max(self.maxi, leftsum + node.val + rightsum)
            return node.val + max(leftsum,rightsum)
        solve(root)
        return self.maxi

Solution = Solution()
# Example usage:
# Constructing a binary tree
root = TreeNode(-10)
root.left = TreeNode(9) 
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution.maxPathSum(root))  # Output: 42 (the path is 15 -> 20 -> 7)
print(Solution.maxPathSum(TreeNode(-3)))  # Output: -3 (single node tree)

        