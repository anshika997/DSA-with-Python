class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1, root2):

        result_1 = []
        result_2 = []

        def getLeaves(node, result):

            if node is None:
                return

            if node.left is None and node.right is None:
                result.append(node.val)
                return

            getLeaves(node.left, result)
            getLeaves(node.right, result)

        getLeaves(root1, result_1)
        getLeaves(root2, result_2)

        return result_1 == result_2


# Tree 1
#
#        3
#       / \
#      5   1
#     / \   \
#    6   2   9
#       / \
#      7   4

root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.right.right = TreeNode(9)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)


# Tree 2
#
#        3
#       / \
#      5   1
#     / \   \
#    6   2   9
#       / \
#      7   4

root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(2)
root2.right.right = TreeNode(9)
root2.left.right.left = TreeNode(7)
root2.left.right.right = TreeNode(4)


# Calling the solution
solution = Solution()
result = solution.leafSimilar(root1, root2)

print("Are the trees leaf-similar?", result)