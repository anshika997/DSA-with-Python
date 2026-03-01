# 📘 Longest Common Prefix -- Beginner Friendly Explanation (Hinglish)

## ✅ Problem Statement

Given a list of strings, find the **longest common prefix** among them.

Example:

    Input: ["flower", "flow", "flight"]
    Output: "fl"

If no common prefix exists → return empty string "".

------------------------------------------------------------------------

## 🧠 Basic Idea

Common prefix matlab: \> Sabhi words ke starting ke same letters jab tak
match karein.

Example:

    flower
    flow
    flight

Compare column-wise:

    f l o w e r
    f l o w
    f l i g h t
    ↑ ↑ ❌ (mismatch)

Answer = **"fl"**

------------------------------------------------------------------------

## ✅ Important Concepts

### 1️⃣ List of Strings

    strs = ["flower", "flow", "flight"]

Structure:

    Index   Word
    0       flower
    1       flow
    2       flight

------------------------------------------------------------------------

### 2️⃣ Indexing Basics

#### Single Indexing

    strs[0] → "flower"

Selects first word.

------------------------------------------------------------------------

#### Double Indexing (MOST IMPORTANT ⭐)

    strs[0][i]

Means:

1.  `strs[0]` → choose word `"flower"`
2.  `[i]` → choose character inside that word

Example:

  Code             Result
  ---------------- --------
  strs\[0\]\[0\]   f
  strs\[0\]\[1\]   l
  strs\[0\]\[2\]   o

Formula:

    list[word_index][character_index]

------------------------------------------------------------------------

### 3️⃣ Why `len(strs[0])` ?

    len("flower") = 6

We loop through characters of first word because:

👉 Common prefix **cannot be longer** than a word.

------------------------------------------------------------------------

## 🔁 Main Loop Explanation

    for i in range(len(strs[0])):

Meaning: - Go through each character position. - i becomes:
`0,1,2,3,4,5`

------------------------------------------------------------------------

### Character Selection

    char = strs[0][i]

Example:

    i = 0 → 'f'
    i = 1 → 'l'
    i = 2 → 'o'

We compare this character with all words.

------------------------------------------------------------------------

## ✅ Complete Code

``` python
class Solution:
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""

        prefix = ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for word in strs:
                if i >= len(word) or word[i] != char:
                    return prefix

            prefix += char

        return prefix
```

------------------------------------------------------------------------

## 🔍 Line-by-Line Logic

### Edge Case

    if not strs:
        return ""

If list empty → no prefix.

------------------------------------------------------------------------

### Prefix Storage

    prefix = ""

Stores matching letters.

------------------------------------------------------------------------

### Outer Loop

Checks character positions.

------------------------------------------------------------------------

### Inner Loop

Checks same position in every word.

------------------------------------------------------------------------

### Stop Condition

    if i >= len(word) or word[i] != char:

Stop when: - word ends OR - characters differ.

------------------------------------------------------------------------

## ⏱ Time Complexity

    O(n × m)

n = number of words\
m = smallest word length

------------------------------------------------------------------------

## ⭐ Memory Trick

    strs[0]     → first word
    strs[0][i]  → ith letter

Compare letters column-wise until mismatch.

------------------------------------------------------------------------

## 🎯 Real-Life Analogy

    Bookshelf → Book → Letter

    strs[word][character]

------------------------------------------------------------------------

## ✅ Final Summary

  Concept          Meaning
  ---------------- -------------------
  strs             list of words
  strs\[0\]        first word
  len(strs\[0\])   number of letters
  strs\[0\]\[i\]   ith letter
  prefix           answer string

------------------------------------------------------------------------

✨ Now you understand: - Indexing - Double indexing - Loop logic -
Longest Common Prefix solution
