class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root):

        if root is None:
            return []

        result = []

        def dfs(node, path):

            path = path + str(node.val)

            if node.left is None and node.right is None:
                result.append(path)
                return

            if node.left:
                dfs(node.left, path + "->")

            if node.right:
                dfs(node.right, path + "->")

        dfs(root, "")

        return result


# Create Tree
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.right = TreeNode(5)


# Run
solution = Solution()

print(solution.binaryTreePaths(root))