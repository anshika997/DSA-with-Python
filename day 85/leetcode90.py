class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def check (self,root,mn,mx):
        if root is None :
            return True 
        if root.val<mn or root.val>mx:
            return False 
        checkLeft = self.check(root.left,mn,root.val-1)
        checkRight = self.check(root.right,root.val+1,mx)
        return checkLeft and checkRight 

    def isValidBST(self, root):
        return self.check(root,-10000000000000,10000000000000)
object = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(object.isValidBST(root))

# Example usage: