class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):

        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        if not self.isSameTree(p.left, q.left):
            return False

        if not self.isSameTree(p.right, q.right):
            return False

        return True


# Tree 1
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)


# Tree 2
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)


# Create object
solution = Solution()

# Check
print(solution.isSameTree(p, q))