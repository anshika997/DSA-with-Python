from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = []

    def preorder(self, root):
        if root is None:
            return

        self.ans.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.preorder(root)
        return self.ans


# Example Tree for testing
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

obj = Solution()
print(obj.preorderTraversal(root))