class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root, low, high):
        total = 0

        if root is None :
            return 0
        if low <= root.val <= high:
            total += root.val
        total += self.rangeSumBST(root.left, low, high)
        total += self.rangeSumBST(root.right, low, high)
        return total
root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(15)

root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

root.right.right = TreeNode(18)

solution = Solution()

print(solution.rangeSumBST(root, 7, 15))
        