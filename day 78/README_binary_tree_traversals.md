# 📚 Binary Tree Traversals (Preorder, Inorder, Postorder)

This project explains three important **Binary Tree Traversal
techniques** using **Python recursion**.

Binary Tree Traversal means **visiting every node of the tree in a
specific order**.

The three main traversal methods are:

1.  Preorder Traversal\
2.  Inorder Traversal\
3.  Postorder Traversal

------------------------------------------------------------------------

# 🌳 Binary Tree Node Structure

``` python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Explanation

-   `class TreeNode` → Blueprint for creating tree nodes\
-   `__init__` → Constructor called when node is created\
-   `val` → Stores node value\
-   `left` → Points to left child\
-   `right` → Points to right child

Example Tree

          1
         / \
        2   3
       / \
      4   5

------------------------------------------------------------------------

# 1️⃣ Preorder Traversal

### Order

Root → Left → Right

### Example Output

    [1, 2, 4, 5, 3]

### Python Code

``` python
class Solution:
    def __init__(self):
        self.ans = []

    def preorder(self, root):
        if root is None:
            return

        self.ans.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def preorderTraversal(self, root):
        self.ans = []
        self.preorder(root)
        return self.ans
```

### Explanation

-   Visit root node first\
-   Traverse left subtree\
-   Traverse right subtree

------------------------------------------------------------------------

# 2️⃣ Inorder Traversal

### Order

Left → Root → Right

### Example Output

    [4, 2, 5, 1, 3]

### Python Code

``` python
class Solution:
    def __init__(self):
        self.ans = []

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)

    def inorderTraversal(self, root):
        self.ans = []
        self.inorder(root)
        return self.ans
```

### Explanation

1.  Traverse left subtree\
2.  Visit root node\
3.  Traverse right subtree

------------------------------------------------------------------------

# 3️⃣ Postorder Traversal

### Order

Left → Right → Root

### Example Output

    [4, 5, 2, 3, 1]

### Python Code

``` python
class Solution:
    def __init__(self):
        self.ans = []

    def postorder(self, root):
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.val)

    def postorderTraversal(self, root):
        self.ans = []
        self.postorder(root)
        return self.ans
```

### Explanation

1.  Traverse left subtree\
2.  Traverse right subtree\
3.  Visit root node

------------------------------------------------------------------------

# 🔁 Traversal Comparison

  Traversal   Order
  ----------- ---------------------
  Preorder    Root → Left → Right
  Inorder     Left → Root → Right
  Postorder   Left → Right → Root

------------------------------------------------------------------------

# ⏱ Time Complexity

O(n) --- each node is visited exactly once.

# 💾 Space Complexity

O(h) --- recursion stack where **h = height of tree**.

Worst case: O(n)

------------------------------------------------------------------------

# 🧠 Concepts Used

-   Binary Tree
-   Recursion
-   Object-Oriented Programming (OOP)

------------------------------------------------------------------------

⭐ This implementation demonstrates how recursive traversal works for
**Preorder, Inorder, and Postorder Binary Tree Traversals in Python.**
