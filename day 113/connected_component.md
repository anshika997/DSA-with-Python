# 🌐 Connected Components in Graphs – README

---

## 🧩 Problem Understanding

In graph problems, you are often given:

* `n` nodes (0 to n-1)
* a list of edges

Even if the graph looks **disconnected**, it is still treated as **one graph with multiple connected components**.

---

## 🧠 What is a Connected Component?

A **connected component** is:

> A group of nodes where each node is reachable from any other node in that group.

---

## 🔍 Example

```
Graph:

0 — 1       3 — 4

2            5
```

### Components:

* Component 1 → {0,1}
* Component 2 → {2}
* Component 3 → {3,4}
* Component 4 → {5}

👉 Total = **4 connected components**

---

## 💡 Core Idea

To find number of components:

1. Use a `visited` array
2. Traverse all nodes
3. If a node is **not visited**:

   * Start DFS/BFS
   * Mark all reachable nodes
   * Increase component count

---

## 🚀 Approach (DFS)

### Steps:

1. Build adjacency list
2. Create `visited` array
3. Loop through all nodes:

   * If not visited → call DFS
   * Increment count
4. Return count

---

## ✅ Code (DFS)

```python
def countComponents(n, edges):
    adj = [[] for _ in range(n)]

    # Step 1: Build graph
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n

    # Step 2: DFS function
    def dfs(node):
        visited[node] = True
        for nei in adj[node]:
            if not visited[nei]:
                dfs(nei)

    count = 0

    # Step 3: Traverse all nodes
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1

    return count
```

---

## 🔄 BFS Alternative

Instead of DFS, you can also use BFS:

```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for nei in adj[node]:
            if not visited[nei]:
                visited[nei] = True
                queue.append(nei)
```

---

## ⚠️ Important Points

* Graph may be **disconnected**
* Always loop through all nodes
* DFS/BFS ensures full traversal of one component
* Each new DFS/BFS call = new component

---

## ⏱️ Complexity

* **Time:** O(n + e)
* **Space:** O(n + e)

---

## 🔥 Applications

This concept is used in:

* Number of Islands
* Number of Provinces
* Friend Circles
* Network Connectivity problems

---

## 🎯 Key Intuition

> “हर unvisited node से traversal शुरू करो → जितनी बार traversal शुरू होगा = उतने connected components”

---

## 🧠 One-Line Summary

👉 Traverse all nodes + start DFS on unvisited = count components

---
