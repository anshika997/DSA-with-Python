class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        
        if root is None:
            return None

        # Swap left and right
        root.left, root.right = root.right, root.left

        # Invert left subtree
        self.invertTree(root.left)

        # Invert right subtree
        self.invertTree(root.right)

        return root


# Create Tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right = TreeNode(9)


# Function to print tree in preorder
def preorder(root):
    if root is None:
        return

    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)


solution = Solution()

print("Before Inverting:")
preorder(root)

solution.invertTree(root)

print("\nAfter Inverting:")
preorder(root)