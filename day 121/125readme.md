# 📝 Letter Combinations of a Phone Number (LeetCode 17) – README

---

## 🧩 Problem

Given a string `digits` (2–9), return all possible letter combinations based on phone keypad mapping.

👉 Example:

```text
Input: "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

---

## 💡 Approach (Backtracking – Simple Idea)

### 🔑 Key Concept:

* Each digit maps to multiple letters
* We need **all possible combinations**
* Build combinations **step by step**

---

## 📱 Phone Mapping

```text
2 → abc  
3 → def  
4 → ghi  
5 → jkl  
6 → mno  
7 → pqrs  
8 → tuv  
9 → wxyz  
```

---

## 🚀 Code

```python
class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []

        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = []

        def solve(index, path):
            if index == len(digits):
                result.append(path)
                return

            for ch in phone[digits[index]]:
                solve(index + 1, path + ch)

        solve(0, "")
        return result
```

---

## 🔍 Dry Run

### Input:

```text
digits = "23"
```

---

### Step 1:

```text
Start → solve(0, "")
```

---

### Step 2:

```text
Digit '2' → a, b, c
```

---

### Step 3:

```text
"a" → solve(1, "a")
"b" → solve(1, "b")
"c" → solve(1, "c")
```

---

### Step 4:

```text
Digit '3' → d, e, f
```

---

### Step 5:

```text
ad, ae, af
bd, be, bf
cd, ce, cf
```

---

### ✅ Final Output:

```python
["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

---

## 🧠 How Backtracking Works

👉 Step-by-step:

```text
Pick a letter → move to next digit → repeat → store result
```

👉 Then:

```text
Go back → try next letter
```

---

## 🌳 Visualization (Tree)

```text
        ""
      / | \
     a  b  c
    /|\ /|\ /|\
   d e f ...
```

---

## ⏱️ Complexity

* **Time Complexity:** O(4^N)
* **Space Complexity:** O(N)

---

## ⚠️ Important Points

* Handle empty input
* Use recursion for all combinations
* Each digit creates multiple branches

---

## 🎯 One-line Summary

👉 “Har digit ke letters ko recursively combine karo”

---

## 💬 Final Note

✔ Most common backtracking problem
✔ Helps in recursion understanding
✔ Same pattern used in:

* Permutations
* Subsets
* Combination problems

---
