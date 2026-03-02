# Stack Implementation Using Linked List (Python)

## 📌 Overview

This project implements a **Stack Data Structure** using a **Linked
List** in Python with Object-Oriented Programming (OOP) concepts.

A **stack** follows the principle:

> **LIFO (Last In First Out)** --- the last element added is the first
> one removed.

------------------------------------------------------------------------

## 🧠 OOP Concepts Used

### 1. Class and Object

-   `Node` class → represents a single element in the stack.
-   `stack` class → manages stack operations.

### 2. Encapsulation

Each node keeps its own data and link together:

``` python
self.data
self.next
```

### 3. Abstraction

The user only calls:

``` python
s.push(10)
```

The internal linking logic is hidden.

------------------------------------------------------------------------

## 📂 Code Structure

### Node Class

``` python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Each node contains: - `data` → value stored - `next` → reference to next
node

Visual:

    [data | next]

------------------------------------------------------------------------

### Stack Class Initialization

``` python
class stack:
    def __init__(self):
        self.top = None
        self.length = 0
```

Meaning: - `top` → points to top element of stack - `length` → number of
elements

Initially:

    top → None

------------------------------------------------------------------------

## ⭐ Push Operation (Important Part)

``` python
def push(self, x):
    self.length += 1

    if self.top == None:
        self.top = Node(x)
        return
    else:
        newNode = Node(x)
        newNode.next = self.top
        self.top = newNode
```

------------------------------------------------------------------------

## 🔍 Line-by-Line Explanation

### Step 1: Create New Node

``` python
newNode = Node(x)
```

Creates a new node.

Example:

    [20 | None]

------------------------------------------------------------------------

### Step 2: Connect New Node to Old Top ⭐

``` python
newNode.next = self.top
```

The new node points to the previous top.

Before:

    top → [10 | None]

After:

    [20 | ] → [10 | None]

------------------------------------------------------------------------

### Step 3: Update Top Pointer ⭐

``` python
self.top = newNode
```

Now the new node becomes the top.

Final Stack:

    top
     ↓
    [20] → [10] → None

------------------------------------------------------------------------

## ❗ Why This Order Matters

Correct Order: 1. Create node 2. Connect to old top 3. Move top pointer

Wrong Order breaks the structure.

------------------------------------------------------------------------

## 🍽️ Real-Life Analogy (Plate Stack)

Adding a plate: 1. Hold new plate (create node) 2. Place above old plate
(connect) 3. New plate becomes top

------------------------------------------------------------------------

## 📊 Example Execution

    push(10)
    push(20)
    push(30)

Result:

    top
     ↓
    [30] → [20] → [10] → None

------------------------------------------------------------------------

## 🧩 Key Concept Summary

  Line                        Meaning
  --------------------------- -------------------
  `newNode = Node(x)`         Create node
  `newNode.next = self.top`   Link to old stack
  `self.top = newNode`        Update top

------------------------------------------------------------------------

## 🧠 Memory Trick

    CREATE → CONNECT → SHIFT TOP

or

    Node banao → old top se jodo → top update karo

------------------------------------------------------------------------

## ✅ Conclusion

This implementation demonstrates: - Stack using Linked List - Pointer
manipulation - Core OOP principles - LIFO behavior

This logic is commonly asked in **exams**, **DSA interviews**, and
**coding practice**.

------------------------------------------------------------------------

✨ Happy Coding!
