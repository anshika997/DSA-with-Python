class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def searchBST(self, root,target):
        if root ==None:
            return None
        curr = root 
        while curr!=None:
                
            if curr.val == target:
                return curr
            elif target < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        return None
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

obj = Solution()
print(obj.searchBST(root, 7).val)  # Output: 7
print(obj.searchBST(root, 4))        # Output: None

        