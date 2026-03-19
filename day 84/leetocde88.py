class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root,target):
        newNode = TreeNode(target)
        if root == None :
            return newNode
        curr = root 
        while curr != None:
            if target < curr.val:
                # left 
                if curr.left!=None:

                    curr = curr.left   
                else :
                    curr.left = newNode
                    break 

            else:

                if  curr.right!=None:

                    curr = curr.right    
                else :
                    curr.right = newNode
                    break 
        return root
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

obj = Solution()
print(obj.insertIntoBST(root, 6).left.right.val)  # Output: 7
print(root.left.right.left.val)  # Output: 6