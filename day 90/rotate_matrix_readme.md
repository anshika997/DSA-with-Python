
# Rotate Image (LeetCode 48) - Detailed README

## Problem
Given an n x n 2D matrix, rotate the image by 90 degrees (clockwise) in-place.

---

## Approach (Very Important)

We solve in 2 steps:

1. **Transpose the matrix**
2. **Reverse each row**

---

## Code 

```python
class Solution:
    def rotate(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        # Step 1: Transpose
        for i in range(row):
            for j in range(i + 1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for k in range(row):
            matrix[k].reverse()
```

---

## Example

Input:
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

---

## Step-by-Step Dry Run

### Step 1: Transpose

Swap matrix[i][j] with matrix[j][i]

Result:
[
 [1,4,7],
 [2,5,8],
 [3,6,9]
]

---

## Why j starts from (i+1)?

To avoid:
- Re-swapping same elements
- Swapping diagonal

---

## Step 2: Reverse Each Row

Row 1: [1,4,7] → [7,4,1]  
Row 2: [2,5,8] → [8,5,2]  
Row 3: [3,6,9] → [9,6,3]

---

## Final Output

[
 [7,4,1],
 [8,5,2],
 [9,6,3]
]

---

## Key Concepts

- Transpose = rows ↔ columns
- Reverse rows = final rotation
- In-place (no extra space)

---

## Time Complexity

O(n^2)

---

## Space Complexity

O(1)

---

## Easy Trick

👉 Transpose + Reverse = 90° rotation

