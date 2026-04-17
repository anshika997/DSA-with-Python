# 📘 Graph Representation in Python – Notes

---

## 🔹 Graph Input Basics

Most graph problems provide:

* `n` → number of nodes
* `m` → number of edges
* List of edges (connections)

👉 Graphs can be:

* **0-indexed** → nodes from `0 to n-1`
* **1-indexed** → nodes from `1 to n`

---

## 🧱 Ways to Represent Graphs

---

# 🔸 1. Adjacency Matrix

### ✅ Concept

* Use a **2D list (matrix)**
* Size: `(n+1) x (n+1)` (for 1-indexed)

👉 If edge exists → mark `1`
👉 If no edge → `0`

---

### 💻 Example

```python
n = 3
adj = [[0]*(n+1) for _ in range(n+1)]

# edge between 1 and 2
adj[1][2] = 1
adj[2][1] = 1   # for undirected
```

---

### ⚖️ Complexity

* **Space:** O(n²) ❌ (high)
* **Time:** O(1) for checking edge

---

### 👍 Pros

* Simple to implement
* Easy edge checking

### 👎 Cons

* Wastes space for sparse graphs

---

# 🔸 2. Adjacency List (MOST IMPORTANT)

### ✅ Concept

* Use a **list of lists**
* Store only connected nodes

---

### 💻 Example

```python
n = 3
adj = [[] for _ in range(n+1)]

# edge between 1 and 2
adj[1].append(2)
adj[2].append(1)   # for undirected
```

---

### ⚖️ Complexity

* **Space:** O(2E) ✅ (efficient)

---

### 👍 Pros

* Memory efficient
* Best for interviews
* Works well with BFS, DFS

### 👎 Cons

* Slightly complex than matrix

---

# 🔸 3. Adjacency Dictionary

### ✅ Concept

* Use a **dictionary**
* Map node → list of neighbors

---

### 💻 Example

```python
graph = {}

graph[1] = [2]
graph[2] = [1]
```

---

### 👍 Pros

* Flexible
* Good for dynamic graphs

### 👎 Cons

* Slightly slower
* Not preferred in interviews

---

# ⚖️ Weighted Graph Representation

👉 Instead of storing `1`, store weight

---

### 💻 Example (Adj List with Weight)

```python
adj = [[] for _ in range(n+1)]

# edge 1 → 2 with weight 5
adj[1].append((2, 5))
adj[2].append((1, 5))
```

---

# 🔀 Directed Graph Representation

👉 Store only **one direction**

---

### 💻 Example

```python
adj[1].append(2)   # 1 → 2
# do NOT add adj[2].append(1)
```

---

## 💡 Key Takeaways

* **Adjacency Matrix** → simple but high space
* **Adjacency List** → best & most used ✅
* **Dictionary** → flexible but less common

---

## 🔥 Quick Revision

* Matrix → O(n²) space
* List → O(E) space
* Directed → one-way storage
* Weighted → store (node, weight)

---

## ✅ Conclusion

👉 For coding interviews and real problems:
**Adjacency List is the best choice** 🚀

It is efficient, scalable, and works perfectly with graph algorithms like:

* BFS
* DFS
* Shortest Path
