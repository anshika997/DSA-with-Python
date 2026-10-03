class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root, val):

        if root is None:
            return None

        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)

        if val > root.val:
            return self.searchBST(root.right, val)

        return None


# Creating the BST
#
#         4
#        / \
#       2   7
#      / \
#     1   3

root = TreeNode(4)

root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


# Value we want to search
val = 2


# Calling the solution
solution = Solution()
result = solution.searchBST(root, val)


# Function to print the subtree
def printTree(root):
    if root is None:
        return

    print(root.val, end=" ")
    printTree(root.left)
    printTree(root.right)


# Printing the result
if result:
    print("Found subtree:")
    printTree(result)
else:
    print("Node not found")