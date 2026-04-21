# 📝 Depth First Search (DFS) in Graph – README

---

## 🧩 Topic

Depth First Search (DFS) – Graph Traversal
(Based on Code & Debug Video – Part 121)

---

## 🧠 What is DFS?

👉 DFS is a graph traversal technique where:

```text
We go as deep as possible in one direction before coming back (backtracking)
```

👉 It uses:

* Recursion
* Visited array

---

## 💡 Intuition

Think like this 👇

👉 “Start from one node → go to its neighbor → then its neighbor → keep going deep”

👉 When no more nodes:

```text
Backtrack and explore other paths
```

---

## 🔗 Given Graph

```text
1 → [2,4]
2 → [1,3,6]
3 → [2]
4 → [1,5,7]
5 → [4,8]
6 → [2]
7 → [4,8]
8 → [5,7]
```

---

## 🚀 Code

```python
from collections import deque   # (not needed in DFS, but imported)

def DFS(node, result, visited, adj):
    visited[node] = 1
    result.append(node)

    for n in adj[node]:
        if visited[n] == 0:
            DFS(n, result, visited, adj)


number_of_nodes = 8

adj = [[],[2,4],[1,3,6],[2],[1,5,7],[4,8],[2],[4,8],[5,7]]

visited = [0] * (number_of_nodes + 1)
result = []

DFS(1, result, visited, adj)

print(result)
```

---

## 🔍 Code Explanation (Step-by-Step)

### 🔹 `visited[node] = 1`

👉 Mark node as visited
👉 Avoid revisiting (prevents infinite loop)

---

### 🔹 `result.append(node)`

👉 Store traversal order

---

### 🔹 `for n in adj[node]`

👉 Explore neighbors

---

### 🔹 `if visited[n] == 0`

👉 Visit only unvisited nodes

---

### 🔹 `DFS(n, ...)`

👉 Recursive call → go deeper

---

## 🔥 Dry Run

Start:

```text
DFS(1)
```

---

### Step-by-step traversal:

```text
1 → 2 → 3 → (back)
         → 6 → (back)
    → (back to 1)
    → 4 → 5 → 8 → 7
```

---

### Final Output:

```text
[1, 2, 3, 6, 4, 5, 8, 7]
```

---

## 🧠 Why this order?

👉 DFS goes deep first:

* From 1 → 2 → 3
* Backtrack → 6
* Backtrack → 4 → 5 → 8 → 7

---

## ⏱️ Complexity

### Time Complexity:

```text
O(N + 2E)
```

👉 Visit all nodes and edges

---

### Space Complexity:

```text
O(N)
```

👉 Visited array + recursion stack

---

## ⚠️ Important Points

* Use `visited` to avoid infinite loops
* Recursion handles backtracking
* Works on both:

  * Directed graphs
  * Undirected graphs

---

## 🔄 BFS vs DFS

| BFS           | DFS              |
| ------------- | ---------------- |
| Queue         | Recursion        |
| Level-wise    | Depth-wise       |
| Shortest path | Deep exploration |

---

## 🎯 One-line Summary

👉 “Go deep first, then backtrack and explore remaining nodes”

---

## 💬 Final Note

✔ Clean recursive implementation
✔ Strong foundation for graph problems
✔ Used in:

* Cycle detection
* Connected components
* Topological sort

---
