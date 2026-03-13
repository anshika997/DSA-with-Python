class treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.ans = []
        
    def inorder (self,root):
        
        if root is None :
            return 
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)
        return self.ans
    
obj = Solution()
root = treenode(1)
root.right = treenode(2)    
root.right.left = treenode(3)
root.left = treenode(4)
print(obj.inorder(root))
# expected_output = [4, 1, 3, 2]