# 📝 Number of Provinces (LeetCode 547) – BFS README

---

## 🧩 Problem

**Number of Provinces**

You are given an `n x n` matrix `isConnected` where:

* `isConnected[i][j] = 1` → city `i` is connected to city `j`
* `0` → not connected

👉 A **province** is a group of directly or indirectly connected cities.

👉 Return the **total number of provinces**.

---

## 💡 Approach (BFS – Your Code Logic)

### Idea:

* Use a **visited array** to track visited cities
* Traverse each city
* If city is **not visited**:

  * Run **BFS**
  * Mark all connected cities
  * Increase province count

---

## 🚀 Code

```python
from collections import deque

class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [0] * n

        def bfs_graph(starting_node):
            queue = deque()
            queue.append(starting_node)
            visited[starting_node] = 1

            while len(queue) != 0:
                e = queue.popleft()

                for node in range(n):
                    if isConnected[e][node] == 1 and visited[node] == 0:
                        queue.append(node)
                        visited[node] = 1

        count = 0

        for i in range(n):
            if visited[i] == 0:
                bfs_graph(i)
                count += 1

        return count
```

---

## 🔍 Dry Run

### Example 1:

```text
Input:
[[1,0,0],
 [0,1,0],
 [0,0,1]]

Output: 3
```

👉 Each node is isolated → 3 provinces

---

### Example 2:

```text
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]

Output: 2
```

👉 {0,1} → 1 province
👉 {2} → 1 province

---

## 🧠 Key Concepts

* BFS explores all connected nodes
* Each BFS call covers **one component**
* Counting BFS calls = number of provinces

---

## ⏱️ Complexity

* **Time Complexity:** O(n²)
* **Space Complexity:** O(n)

---

## ⚠️ Important Points

* Graph is given as **adjacency matrix**
* Use `range(n)` instead of adjacency list
* Mark visited nodes to avoid repetition
* Queue ensures level-by-level traversal

---

## 🎯 One-line Summary

👉 “Run BFS on every unvisited node → count provinces”

---

## 💬 Final Note

✔ Clean BFS implementation
✔ Direct application of graph traversal
✔ Strong foundation for advanced graph problems

---
