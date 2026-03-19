# Delete Node in BST (Binary Search Tree)

## Problem

Delete a node with a given key from a BST and return the updated root.

------------------------------------------------------------------------

## Code

``` python
class Solution:
    def deleteNode(self, root, key):

        if root is None: 
            return None 

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if root.left is None and root.right is None:
                return None 

            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            else:
                temp = root.right
                while temp.left != None:
                    temp = temp.left

                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)

        return root
```

------------------------------------------------------------------------

## Concept

There are 3 cases in deletion:

1.  No child → delete directly\
2.  One child → replace with child\
3.  Two children →
    -   Find inorder successor (smallest in right subtree)\
    -   Replace value\
    -   Delete that successor

------------------------------------------------------------------------

## Dry Run

Initial Tree:

        10
       /  \
      5    15
     / \   / \
    2   7 12 20

Delete key = 10

Step 1: Node found (10)

Step 2: It has two children

Step 3: Find smallest in right subtree → 12

Step 4: Replace 10 with 12

Step 5: Delete original 12 from right subtree

Final Tree:

        12
       /  \
      5    15
     / \     \
    2   7     20

------------------------------------------------------------------------

## Output Check

Before: 10\
After: 12

------------------------------------------------------------------------

## Key Points

-   Always return root after changes\
-   Use recursion to reach the node\
-   Inorder successor is used for 2-child case
