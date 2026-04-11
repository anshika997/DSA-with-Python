# 🌳 Binary Tree Maximum Path Sum – README

## 🧩 Problem Statement

Given a binary tree, find the **maximum path sum**.

* A path can start and end at **any node**
* A path must be **continuous (connected)**
* It does **not need to pass through the root**

---

## 💡 Key Idea

At each node, we consider two things:

1. **Path passing through the node**
   → `left + node + right`
   (This could be the final answer)

2. **Path going upward (to parent)**
   → `node + max(left, right)`
   (Because path cannot split upward)

---

## 🚀 Approach (DFS + Recursion)

* Traverse the tree using **DFS**
* At each node:

  * Get max sum from left subtree
  * Get max sum from right subtree
  * Ignore negative sums (they reduce total)
  * Update global maximum
  * Return best single path to parent

---

## ✅ Algorithm Steps

1. Initialize `maxi = -∞`
2. Define recursive function:

   * If node is `None` → return `0`
   * Recursively compute `leftsum` and `rightsum`
   * If any sum is negative → make it `0`
   * Update:

     ```
     maxi = max(maxi, leftsum + node.val + rightsum)
     ```
   * Return:

     ```
     node.val + max(leftsum, rightsum)
     ```
3. Call recursion on root
4. Return `maxi`

---

## 🧠 Code

```python
class Solution:
    def maxPathSum(self, root):
        self.maxi = float('-inf')

        def solve(node):
            if node is None:
                return 0

            leftsum = solve(node.left)
            if leftsum < 0:
                leftsum = 0

            rightsum = solve(node.right)
            if rightsum < 0:
                rightsum = 0

            self.maxi = max(self.maxi, leftsum + node.val + rightsum)

            return node.val + max(leftsum, rightsum)

        solve(root)
        return self.maxi
```

---

## ⚠️ Important Concepts

### 🔹 Why ignore negative values?

Negative paths reduce total sum → बेहतर है उन्हें छोड़ देना

---

### 🔹 Why global variable (`self.maxi`)?

Because best path:

* may not pass through root
* can be anywhere in tree

---

### 🔹 Why return only one side?

Because path cannot branch upward
(parent can only choose one direction)

---

## ⏱️ Complexity

* **Time:** `O(n)` (visit each node once)
* **Space:** `O(h)` (recursion stack, height of tree)

---

## 🔥 Example

```
        -10
       /    \
      9     20
           /  \
          15   7
```

👉 Maximum Path:

```
15 → 20 → 7 = 42
```

---

## 🎯 Summary

* Use DFS
* Ignore negative paths
* Track global maximum
* Return only one branch upward

---

## 🧠 One-Line Intuition

👉 *“हर node को center मानकर best path निकालो और global maximum update करते जाओ”*
