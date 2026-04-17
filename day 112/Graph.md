# 📘 Graph Data Structures – Introduction (Notes)

---

## 🔹 What is a Graph?

A **Graph** is a data structure used to represent relationships between objects.

* It consists of:

  * **Nodes (Vertices)** → represent entities
  * **Edges** → represent connections between nodes

---

## 🧱 Basic Components

### ✅ Nodes (Vertices)

* Fundamental units of a graph
* Represent data points

### ✅ Edges

* Connections between nodes
* Can be **directed** or **undirected**

---

## 🔀 Types of Graphs

### 🔸 Undirected Graph

* Edges have **no direction**
* Travel is possible **both ways**

👉 Example:
A — B (you can go A → B and B → A)

---

### 🔸 Directed Graph (Digraph)

* Edges have **direction (arrows)**
* Travel is **one-way**

👉 Example:
A → B (only A → B, not B → A)

---

## 🔁 Cycle in Graph

* A **cycle** exists if:

  * You start from a node
  * Travel through edges
  * Come back to the same node

👉 Example:
A → B → C → A

---

## 🚫 DAG (Directed Acyclic Graph)

* A **Directed Graph with NO cycles**

👉 Key Feature:

* No way to return to the starting node

---

## 🛣️ Path

* A **sequence of nodes** connected by edges

👉 Important Rule:

* In a **simple path**, a node is **not repeated**

---

## 📊 Degree of a Node

### 🔸 In Undirected Graph

* **Degree = Number of edges connected to a node**

---

### 🔸 In Directed Graph

* **In-degree** → Number of incoming edges
* **Out-degree** → Number of outgoing edges

---

## ⚖️ Weighted Graph

* Each edge has a **weight (value)**

👉 Represents:

* Distance
* Cost
* Time

---

### 🔹 Unweighted Graph

* If no weight is given → default weight = **1**

---

## 💡 Key Takeaways

* Graph = Nodes + Edges
* Can be **directed or undirected**
* Cycles help detect loops
* DAG = No cycles
* Degree helps understand node connections
* Weights add real-world meaning (cost, distance, etc.)

---

## 🔥 Quick Revision

* Node = point
* Edge = connection
* Cycle = loop
* DAG = no loop
* Path = sequence
* Degree = connections
* Weight = value on edge

---

## ✅ Conclusion

Graphs are powerful structures used in:

* Social networks
* Maps & navigation
* Web connections
* Recommendation systems

👉 Understanding basics is important before learning algorithms like BFS, DFS, Dijkstra, etc. 🚀
