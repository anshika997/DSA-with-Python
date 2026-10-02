class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1, root2):

        # Dono empty
        if root1 is None and root2 is None:
            return None

        # Sirf root2 present
        if root1 is None:
            return root2

        # Sirf root1 present
        if root2 is None:
            return root1

        # Dono nodes present hain
        branch = root1.val + root2.val

        # New merged node
        mergedNode = TreeNode(branch)

        # Left subtree merge
        mergedNode.left = self.mergeTrees(root1.left, root2.left)

        # Right subtree merge
        mergedNode.right = self.mergeTrees(root1.right, root2.right)

        return mergedNode


# -------------------------
# Tree 1
# -------------------------

root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)


# -------------------------
# Tree 2
# -------------------------

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)


# -------------------------
# Merge
# -------------------------

solution = Solution()

mergedRoot = solution.mergeTrees(root1, root2)


# -------------------------
# Print tree - Preorder
# -------------------------

def preorder(root):
    if root is None:
        return

    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)


print("Merged Tree:")
preorder(mergedRoot)