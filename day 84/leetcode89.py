class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root, key):

        if root is None: 
            return None 

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if root.left is None and root.right is None:
                return None 

            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            else:
                temp = root.right
                while temp.left != None:
                    temp = temp.left

                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)

        return root


# -------- Simple Testing --------

# create tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

print("Before:", root.val)   # root value

obj = Solution()
root = obj.deleteNode(root, 10)

print("After:", root.val)    # root changed