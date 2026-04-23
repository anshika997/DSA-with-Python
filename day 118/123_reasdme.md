# 📝 Add Strings (LeetCode 415) – README

---

## 🧩 Problem

**Add Strings**

Given two non-negative integers `num1` and `num2` represented as strings, return their sum as a string.

👉 You are **NOT allowed** to use:

* `int()`
* Built-in big integer libraries

---

## 💡 Approach (Manual Addition)

### Idea:

* Add digits from **right to left** (just like school math)
* Maintain a **carry**
* Store result in reverse, then reverse it at the end

---

## 🚀 Code

```python id="q3l4mn"
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            total = n1 + n2 + carry
            result.append(str(total % 10))
            carry = total // 10

            i -= 1
            j -= 1

        return ''.join(result[::-1])
```

---

## 🔍 Dry Run

### Example:

```text
num1 = "123"
num2 = "456"
```

---

### Step-by-step:

#### Step 1:

```text
3 + 6 = 9
result = ['9']
carry = 0
```

#### Step 2:

```text
2 + 5 = 7
result = ['9','7']
```

#### Step 3:

```text
1 + 4 = 5
result = ['9','7','5']
```

---

### Final:

```text
Reverse → ['5','7','9']
Output → "579"
```

---

## 🔥 Example with Carry

```text
num1 = "99"
num2 = "1"
```

#### Step 1:

```text
9 + 1 = 10 → write 0, carry 1
result = ['0']
```

#### Step 2:

```text
9 + 0 + 1 = 10 → write 0, carry 1
result = ['0','0']
```

#### Step 3:

```text
carry = 1
result = ['0','0','1']
```

---

### Final:

```text
Reverse → "100"
```

---

## 🧠 Key Concepts

* Traverse from **right to left**
* Handle **carry properly**
* Use list for efficient string building
* Reverse result at the end

---

## ⏱️ Complexity

* **Time Complexity:** O(max(n, m))
* **Space Complexity:** O(max(n, m))

---

## ⚠️ Important Points

* Cannot use `int(num1)` or `int(num2)`
* Must simulate addition manually
* Works for very large numbers

---

## 🎯 One-line Summary

👉 “Add digits from right to left with carry and reverse the result”

---

## 💬 Final Note

✔ Simple and interview-friendly solution
✔ Follows constraints correctly
✔ Builds strong base for string + math problems

---
