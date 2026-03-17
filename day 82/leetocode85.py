class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root):
        # base case 
        if root == None:
            return 0 
        # left hight 
        left_hight = self.maxDepth(root.left)
        right_hight = self.maxDepth(root.right)

        return max(left_hight,right_hight) + 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.maxDepth(root))