# 📝 Ransom Note – README (Your Approach)

---

## 🧩 Problem

**Ransom Note**

Given two strings:

* `ransomNote`
* `magazine`

Return **True** if `ransomNote` can be constructed using characters from `magazine`.

👉 Each character in `magazine` can be used **only once**

---

## 💡 Approach (Brute Force + Mark Used)

### Idea:

* Convert `magazine` into a list (so we can modify it)
* For each character in `ransomNote`:

  * Search it in `magazine`
  * If found:

    * Mark that character as used (`#`)
  * If not found:

    * Return False
* If all characters are matched → return True

---

## 🚀 Code

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine = list(magazine)

        for r in ransomNote:
            found = False

            for m in range(len(magazine)):
                if r == magazine[m]:
                    found = True
                    magazine[m] = '#'   # mark as used
                    break

            if not found:
                return False

        return True
```

---

## 🔍 Dry Run

### Example 1:

```text
ransomNote = "aa"
magazine = "aab"
```

Step-by-step:

* magazine → ['a','a','b']
* r = 'a' → found → ['#','a','b']
* r = 'a' → found → ['#','#','b']

👉 return True ✅

---

### Example 2:

```text
ransomNote = "aa"
magazine = "ab"
```

* r = 'a' → found → ['#','b']
* r = 'a' → not found ❌

👉 return False

---

## ⚠️ Key Points

* Strings are **immutable** → convert to list
* Mark used characters to avoid reuse
* Use `found` flag to track matching
* Break loop once character is found

---

## ⏱️ Complexity

* **Time Complexity:** O(n × m)
* **Space Complexity:** O(m)

---

## 🎯 One-line Summary

👉 “For each character in ransomNote, find it once in magazine and mark it used”

---

## 💬 Final Note

✔ Correct logic
✔ Good for learning
⚠️ Can be optimized further using hashmap

---
