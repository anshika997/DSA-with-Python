class treeNode:
    def __init__(self,val):
        self.val=val
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.ans = []
    def postorder(self,root):
        if root is None:
            return 
        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.val)
        return self.ans
    
root = treeNode(1)
root.right = treeNode(2)
root.right.left = treeNode(3)   
root.left = treeNode(4)
obj = Solution()
print(obj.postorder(root))