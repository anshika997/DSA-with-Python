
# Last Stone Weight (Heap + nlargest) - Detailed README

## Problem
Given stones with weights, we repeatedly:
- Take 2 largest stones
- Smash them
- If equal → both destroyed
- Else → push (difference) back

Return the last remaining stone.

---

## Approach

We use a **Max Heap**.

But Python provides only **Min Heap**, so:
👉 We insert negative values to simulate Max Heap.

---

## Code

```python
import heapq

class Solution:
    def lastStoneWeight(self, stones, k):
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)

            diff = a - b

            if diff != 0:
                heapq.heappush(heap, -diff)

        if len(heap) == 0:
            return 0
        else:
            return -heapq.nlargest(k, heap)[-1]
```

---

## Example

Input:
stones = [3,2,1,5,6,4]
k = 1

---

## Detailed Dry Run

### Step 1: Build Heap
Insert negatives:

[-6, -5, -4, -3, -2, -1]

---

### Step 2:
Pop 6 and 5 → diff = 1  
Push -1

Heap:
[-4, -3, -2, -1, -1]

---

### Step 3:
Pop 4 and 3 → diff = 1  
Push -1

Heap:
[-2, -1, -1, -1]

---

### Step 4:
Pop 2 and 1 → diff = 1  
Push -1

Heap:
[-1, -1, -1]

---

### Step 5:
Pop 1 and 1 → diff = 0  
Do nothing

Heap:
[-1]

---

### Step 6: Final Step

heap = [-1]

Using:
heapq.nlargest(1, heap) → [-1]

Return:
-(-1) = 1

---

## Final Output

1

---

## Key Concepts

- Python heap = Min Heap
- Use negative for Max Heap
- nlargest returns largest values (still negative)
- Convert back using minus

---

## Time Complexity

O(n log n)

---

## Space Complexity

O(n)

