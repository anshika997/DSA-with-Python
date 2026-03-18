
# Balanced Binary Tree - Detailed Dry Run README

## Problem
Check whether a binary tree is height-balanced.

A tree is balanced if:
|height(left) - height(right)| <= 1 for every node

---

## Approach (Your Logic)

We use recursion to:
1. Calculate height
2. Check balance at the same time

We use a global variable:
self.ans = True

If any node violates condition:
self.ans = False

---

## Code

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = True

    def height(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height - right_height) > 1:
            self.ans = False

        return max(left_height, right_height) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root)
        return self.ans
```

---

## Example Tree (Unbalanced)

        1
       / \
      2   3
     /
    4
   /
  5

---

## FULL DRY RUN (Step by Step)

### Step 1: Call height(1)

We go LEFT first (recursion always goes deep first)

---

### Step 2: height(2)

---

### Step 3: height(4)

---

### Step 4: height(5)

Node 5:
left = 0
right = 0

height = 1

---

### Step 5: Back to Node 4

left = 1
right = 0

difference = 1 → OK

height = 2

---

### Step 6: Back to Node 2

left = 2
right = 0

difference = 2 → NOT BALANCED

self.ans = False

height = 3

---

### Step 7: Node 3

left = 0
right = 0

height = 1

---

### Step 8: Back to Node 1

left = 3
right = 1

difference = 2 → NOT BALANCED

---

## Final Answer

False

---

## Important Observations

- Recursion goes DEEP first (DFS)
- Height is calculated bottom-up
- Balance is checked at every node
- One violation → whole tree is NOT balanced

---

## Time Complexity

O(N)

Each node is visited once

---

## Space Complexity

O(H)

H = height of tree (recursion stack)

---

## Key Learning

This problem teaches:
- Recursion
- Tree traversal
- Optimized thinking (combine tasks)

