# 📘 Find Duplicate Number – Floyd’s Cycle Detection (README)

---

## 🔹 Problem

Given an array `nums` of size `n + 1` where each number is in the range `1 to n`, find the duplicate number.

---

## 🧠 Approach Used

We use **Floyd’s Cycle Detection Algorithm (Tortoise and Hare)**.

👉 Idea:

* Treat the array like a **linked list**
* Each index points to the next index using its value
* A duplicate number creates a **cycle**
* The start of the cycle = **duplicate number**

---

## 🚀 Code

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # Step 1: Detect cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Step 2: Find duplicate (cycle start)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
```

---

## 🔍 Step-by-Step Explanation

### 1. Initialize Pointers

* `slow` moves **1 step**
* `fast` moves **2 steps**
* Both start from the same position

---

### 2. Detect Cycle

* Move:

  * `slow = nums[slow]`
  * `fast = nums[nums[fast]]`
* If they meet → cycle exists

---

### 3. Find Cycle Start

* Reset `slow` to start
* Move both pointers one step at a time
* Where they meet again = **duplicate number**

---

## 📌 Example

Input:

```
nums = [1,3,4,2,2]
```

Traversal:

```
0 → 1 → 3 → 2 → 4 → 2 → ...
```

Cycle:

```
2 → 4 → 2
```

Output:

```
2
```

---

## ⏱️ Complexity

* **Time:** O(n)
* **Space:** O(1) ✅ (Optimal)

---

## 💡 Key Points

* No extra space used
* Array is not modified
* Works because duplicate guarantees a cycle

---

## 🔥 Interview Explanation

“I treat the array as a linked list where each value points to the next index. Since a duplicate exists, it forms a cycle. Using Floyd’s cycle detection, I first detect the cycle and then find its starting point, which is the duplicate number.”

---

## ✅ Conclusion

This is the most **optimal solution** for the problem:

* Efficient
* Clean logic
* Commonly expected in interviews 🚀
