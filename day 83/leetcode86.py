class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def __init__(self):
        self.ans = True
    def height(self, root):
        # base case 
        if root == None:
            return 0 
        # left hight 
        left_hight = self.height(root.left)
        right_hight = self.height(root.right)
        
        if abs(left_hight-right_hight)>1:
            self.ans = False

        return max(left_hight,right_hight) + 1
    def isBalanced(self, root):
        self.height(root)
        return self.ans
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.isBalanced(root))