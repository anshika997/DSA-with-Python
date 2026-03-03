# Queue Implementation Using Two Stacks (Python)

## 📌 Problem Statement

We need to implement a **Queue** using **Stacks**.

A **Queue** follows:

👉 **FIFO (First In First Out)**
The element inserted first should be removed first.

Example:

```
push(1), push(2), push(3)

Queue: 1 → 2 → 3
pop() → removes 1
```

But a **Stack** follows:

👉 **LIFO (Last In First Out)**
The last inserted element is removed first.

```
Stack:
push(1), push(2), push(3)
pop() → removes 3
```

So stacks behave opposite to queues.

---

## 🎯 Why Do We Use 2 Stacks?

One stack alone cannot maintain FIFO order because it always removes the latest element.

So we use **two stacks** to reverse the order twice.

### Idea:

1. First reversal → change order
2. Second reversal → restore order in queue form

Double reversing helps us simulate queue behavior.

---

## 🧱 Stacks Used in Code

```python
self.st1 = []
self.st2 = []
```

| Stack   | Role            | Purpose                       |
| ------- | --------------- | ----------------------------- |
| **st1** | ✅ Main Stack    | Stores final queue order      |
| **st2** | 🔄 Helper Stack | Used only for moving elements |

---

## 🧠 Concept in Simple Words

Think like this:

* `st1` = Actual queue storage
* `st2` = Temporary table while rearranging items

We move elements back and forth to place the **oldest element at the top**.

---

## ⚙️ Working of Operations

---

## ✅ PUSH Operation (Insert Element)

### Code

```python
while len(self.st1) > 0:
    self.st2.append(self.st1.pop())

self.st1.append(x)

while len(self.st2) > 0:
    self.st1.append(self.st2.pop())
```

### Why move elements?

Stack inserts only at TOP.

But queue needs new element at the **rear (bottom)**.

So we:

1. Empty main stack into helper stack
2. Insert new element
3. Restore old elements back

---

### Dry Run (Step-by-Step)

#### push(1)

```
st1 = [1]
```

Queue:

```
Front → 1
```

---

#### push(2)

**Step 1: Move st1 → st2**

```
st1 = []
st2 = [1]
```

**Step 2: Insert 2**

```
st1 = [2]
```

**Step 3: Move back**

```
st1 = [2,1]
st2 = []
```

Queue view:

```
Front → 1 2
```

---

#### push(3)

Move → Insert → Restore

```
st1 = [3,2,1]
```

Queue
