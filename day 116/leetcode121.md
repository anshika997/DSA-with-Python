# 📝 Keys and Rooms (LeetCode 841) – DFS README

---

## 🧩 Problem

**Keys and Rooms**

You are given `rooms` where:

* `rooms[i]` contains keys to other rooms

👉 You start from **room 0**

👉 Return **True** if you can visit all rooms, otherwise False

---

## 💡 Approach (DFS – Same as Your Code)

### Idea:

* Treat each room as a **node**
* Keys inside room = **neighbors**
* Use **DFS traversal**
* Mark visited rooms
* Finally check if all rooms are visited

---

## 🚀 Code

```python
class Solution:
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [0] * n

        def DFS(node):
            visited[node] = 1

            for nbh in rooms[node]:
                if visited[nbh] == 0:
                    DFS(nbh)

        DFS(0)

        return all(visited)
```

---

## 🔍 Line-by-Line Explanation

### 🔹 `visited = [0] * n`

👉 Track visited rooms
👉 0 = not visited, 1 = visited

---

### 🔹 `DFS(node)`

👉 Recursive function to visit rooms

---

### 🔹 `visited[node] = 1`

👉 Mark current room visited

---

### 🔹 `for nbh in rooms[node]`

👉 Loop through keys (neighbors)

---

### 🔹 `if visited[nbh] == 0`

👉 Visit only unvisited rooms

---

### 🔹 `DFS(0)`

👉 Start from room 0

---

### 🔹 `return all(visited)`

👉 Check if all rooms visited

---

# 🔥 Dry Run 1 (Important)

### Input:

```text
rooms = [[1],[2],[3],[]]
```

---

### Step 1:

```text
visited = [0,0,0,0]
```

Start:

```text
DFS(0)
```

---

### Step 2: Visit Room 0

```text
visited = [1,0,0,0]
keys = [1]
```

👉 Go to room 1

---

### Step 3: Visit Room 1

```text
visited = [1,1,0,0]
keys = [2]
```

👉 Go to room 2

---

### Step 4: Visit Room 2

```text
visited = [1,1,1,0]
keys = [3]
```

👉 Go to room 3

---

### Step 5: Visit Room 3

```text
visited = [1,1,1,1]
keys = []
```

👉 No more rooms

---

### ✅ Final:

```text
all(visited) = True
```

👉 Output: **True**

---

# ❌ Dry Run 2

### Input:

```text
rooms = [[1,3],[3,0,1],[2],[0]]
```

---

### Step 1:

```text
visited = [0,0,0,0]
```

---

### Step 2: DFS(0)

```text
visited = [1,0,0,0]
keys = [1,3]
```

---

### Step 3: DFS(1)

```text
visited = [1,1,0,0]
keys = [3,0,1]
```

---

### Step 4: DFS(3)

```text
visited = [1,1,0,1]
keys = [0]
```

---

### 🚨 Room 2 never visited

```text
visited = [1,1,0,1]
```

---

### ❌ Final:

```text
all(visited) = False
```

👉 Output: **False**

---

# 🧠 Key Concepts

* DFS explores deeply first
* Each room → visit its keys
* Recursion handles traversal
* `visited` prevents infinite loops

---

# ⏱️ Complexity

* **Time:** O(N + E)
* **Space:** O(N) (recursion + visited)

---

# 🎯 One-line Summary

👉 “Start from room 0, use DFS to visit all reachable rooms, check if all visited”

---

# 💬 Final Note

✔ Same logic as your DFS code
✔ Just replaced:

* `node → room`
* `adj → rooms`

👉 You already knew the solution 🔥

---
