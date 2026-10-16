
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findTarget(root, k):
    q = deque()

    if root is not None:
        q.append(root)

    values = []

    # Step 1: BFS traversal
    while q:
        node = q.popleft()
        values.append(node.val)

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)

    # Step 2: Sort the values
    values.sort()

    # Step 3: Two pointers
    n = len(values)
    l = 0
    r = n - 1

    while l < r:
        total = values[l] + values[r]

        if total == k:
            return True
        elif total > k:
            r -= 1
        else:
            l += 1

    return False


# Create a binary tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

# Test cases
print(findTarget(root, 9))   # True: 2 + 7
print(findTarget(root, 28))  # False
print(findTarget(root, 6))   # True: 2 + 4
