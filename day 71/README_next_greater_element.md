# Next Greater Element (Stack Approach)

## Problem Statement

Given two arrays `nums1` and `arr`, find the **next greater element**
for each element in `nums1` using the order of elements in `arr`.

The **Next Greater Element (NGE)** of an element `x` is the **first
greater number to the right of x** in the array.

If there is no greater element to the right, return **-1**.

------------------------------------------------------------------------

## Example

Input:

    nums1 = [4, 1, 2]
    arr   = [1, 3, 4, 2]

Process:

  Element   Right Side   Next Greater
  --------- ------------ --------------
  1         3,4,2        3
  3         4,2          4
  4         2            -1
  2         ---          -1

Dictionary created from `arr`:

    1 → 3
    3 → 4
    4 → -1
    2 → -1

Output for `nums1`:

    [-1, 3, -1]

------------------------------------------------------------------------

# Python Implementation

``` python
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], arr: List[int]) -> List[int]:
        n = len(arr)
        ans = {}
        st = []

        for i in range(n-1, -1, -1):

            while len(st) > 0 and st[-1] <= arr[i]:
                st.pop()

            if len(st) == 0:
                ans[arr[i]] = -1
            else:
                ans[arr[i]] = st[-1]

            st.append(arr[i])

        return [ans[x] for x in nums1]


nums1 = [4,1,2]
arr = [1,3,4,2]

obj = Solution()
print(obj.nextGreaterElement(nums1, arr))
```

------------------------------------------------------------------------

# Algorithm Explanation

## Step 1: Create Data Structures

    ans = {}
    st = []

-   `ans` → dictionary storing next greater element
-   `st` → stack used to track possible greater elements

------------------------------------------------------------------------

## Step 2: Traverse from Right to Left

    for i in range(n-1, -1, -1):

We move **right to left** because the next greater element must appear
**to the right** of the current element.

Example traversal for `[1,3,4,2]`:

    Index : 3 → 2 → 1 → 0
    Value : 2 → 4 → 3 → 1

------------------------------------------------------------------------

## Step 3: Remove Smaller Elements

    while len(st) > 0 and st[-1] <= arr[i]:
        st.pop()

If the stack top is smaller than the current element, it cannot be the
next greater element, so it is removed.

------------------------------------------------------------------------

## Step 4: Assign Next Greater Element

If stack becomes empty:

    ans[arr[i]] = -1

Otherwise:

    ans[arr[i]] = st[-1]

The stack's top element is the next greater element.

------------------------------------------------------------------------

## Step 5: Push Current Element

    st.append(arr[i])

Current element is added to the stack so it can help determine the next
greater element for elements on the left.

------------------------------------------------------------------------

## Step 6: Generate Result

    return [ans[x] for x in nums1]

For every element in `nums1`, we fetch its next greater element from the
dictionary.

------------------------------------------------------------------------

# Time Complexity

  Operation          Complexity
  ------------------ ------------
  Traversing array   O(n)
  Stack operations   O(n)
  Building result    O(m)

Total:

    O(n + m)

Where: - `n` = length of `arr` - `m` = length of `nums1`

------------------------------------------------------------------------

# Space Complexity

    O(n)

Used for: - Stack - Dictionary

------------------------------------------------------------------------

# Key Concept

This problem uses a **Monotonic Stack**.

A monotonic stack helps efficiently solve problems like:

-   Next Greater Element
-   Next Smaller Element
-   Stock Span Problem
-   Daily Temperatures

------------------------------------------------------------------------

# How to Run in VS Code

1.  Create a Python file:

```{=html}
<!-- -->
```
    next_greater_element.py

2.  Paste the Python code.

3.  Run:

```{=html}
<!-- -->
```
    python next_greater_element.py

------------------------------------------------------------------------

# Output

    [-1, 3, -1]

------------------------------------------------------------------------

# Learning Outcome

After completing this problem, you will understand:

-   How **stack data structures** work
-   How to solve **Next Greater Element problems**
-   How **monotonic stack patterns** are used in DSA
