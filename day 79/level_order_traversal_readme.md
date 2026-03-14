
# Binary Tree Level Order Traversal (Queue Implementation)

This README explains a Python implementation of Level Order Traversal (Breadth First Search) of a Binary Tree.

---

# VS Code Runnable Code

Create a file in VS Code:

level_order_traversal.py

Paste the following code:

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Queue:
    def __init__(self):
        self.q = []
        self.front = -1

    def push(self, x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)

    def pop(self):
        if len(self.q) == 0:
            return -1

        x = self.q[self.front]
        self.front += 1

        if self.front == len(self.q):
            self.front = -1
            self.q = []

        return x

    def getfront(self):
        if len(self.q) == 0:
            return -1
        return self.q[self.front]

    def size(self):
        if self.front == -1:
            return 0
        return len(self.q) - self.front


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []

        if root is None:
            return ans

        queue = Queue()
        queue.push(root)

        ans.append([root.val])

        while queue.size() > 0:

            l = queue.size()
            level = []

            for i in range(l):

                front = queue.pop()

                if front.left != None:
                    queue.push(front.left)
                    level.append(front.left.val)

                if front.right != None:
                    queue.push(front.right)
                    level.append(front.right.val)

            if len(level) > 0:
                ans.append(level)

        return ans


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.levelOrder(root))


---

# Example Tree

        3
       / \
      9   20
         /  \
        15   7

Output:

[[3], [9,20], [15,7]]

---

# Detailed Dry Run

Initial

Queue = [3]
Answer = [[3]]

---

Step 1

Remove 3 from queue

Children = 9 and 20

Queue becomes

[9,20]

Level = [9,20]

Answer = [[3], [9,20]]

---

Step 2

Remove 9 and 20

9 has no children

20 has children 15 and 7

Queue becomes

[15,7]

Level = [15,7]

Answer = [[3], [9,20], [15,7]]

---

Step 3

Remove 15 and 7

No children

Queue becomes empty

Algorithm stops

---

Final Answer

[[3], [9,20], [15,7]]

---

Time Complexity

O(N)

Each node is visited once.

Space Complexity

O(N)

Queue stores nodes level by level.
