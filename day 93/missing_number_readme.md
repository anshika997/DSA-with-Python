
# Missing Number - Detailed README

## Problem
Given an array containing `n` distinct numbers in the range [0, n], return the only number that is missing.

---

## Code

```python
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        freq = {}

        for i in range(0, n+1):
            freq[i] = 0

        for num in nums:
            freq[num] = 1

        for k, v in freq.items():
            if v == 0:
                return k
```

---

## Step-by-Step Explanation

### Step 1: Create Frequency Map

```python
for i in range(0, n+1):
    freq[i] = 0
```

👉 Initialize all numbers from 0 to n with value 0  
👉 Means: "Not present yet"

---

### Step 2: Mark Present Numbers

```python
for num in nums:
    freq[num] = 1
```

👉 If number exists in array → mark it as 1

---

## 🔥 Step 3: Find Missing Number (MAIN PART)

```python
for k, v in freq.items():
    if v == 0:
        return k
```

### समझो carefully:

👉 `freq.items()` gives:
```text
(key, value)
```

Example:
```text
0 → 1
1 → 1
2 → 0
3 → 1
```

---

### Loop Breakdown:

```python
for k, v in freq.items():
```

👉 `k` = number  
👉 `v` = 0 or 1  

---

```python
if v == 0:
```

👉 Means: number is NOT present in original array  

---

```python
return k
```

👉 Return that missing number  

---

## Example

Input:
```text
nums = [3,0,1]
```

### Step 1:
```text
freq = {0:0, 1:0, 2:0, 3:0}
```

### Step 2:
```text
freq = {0:1, 1:1, 2:0, 3:1}
```

### Step 3:
```text
Check:
0 → 1 ❌
1 → 1 ❌
2 → 0 ✅ → RETURN 2
```

---

## Final Output

```text
2
```

---

## Time Complexity

O(n)

---

## Space Complexity

O(n)

---

## Key Idea

👉 Store presence using dictionary  
👉 Find the one which is not marked  

