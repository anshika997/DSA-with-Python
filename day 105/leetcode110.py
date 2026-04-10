class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0   # store globally inside class
        
        def solve(node):
            if node is None:
                return 0

            leftHeight = solve(node.left)
            rightHeight = solve(node.right)

            # update diameter
            self.diameter = max(self.diameter, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)

        solve(root)
        return self.diameter
Solution = Solution()
# Example usage:
# Constructing a binary tree
root = TreeNode(1)
root.left = TreeNode(2) 
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(Solution.diameterOfBinaryTree(root))  # Output: 3 (the path is 4 -> 2 -> 1 -> 3)
print(Solution.diameterOfBinaryTree(TreeNode(1)))  # Output: 0 (single node tree)