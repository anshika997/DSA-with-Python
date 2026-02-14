# 📚 DSA — Stack Data Structure (Today's Learning)

## 🥞 1. Introduction to Stack Data Structure

A **Stack** is a linear data structure that follows the **LIFO principle**:

```
Last In → First Out (LIFO)
```

This means the element inserted last is removed first.

### 🎯 Real Life Example

* Stack of plates
* Stack of books
* Browser back button

👉 We always insert and remove elements from the **top** of the stack.

### 📦 Example

```
Push 10
Push 20
Push 30
```

Stack looks like:

```
30 ← Top
20
10
```

If we remove an element → `30` is removed first.

---

## ⚙️ 2. Basic Operations of Stack

### ✅ Push (Insert)

Adds an element to the top of the stack.

```
push(10)
push(20)
```

---

### ✅ Pop (Remove)

Removes the top element from the stack.

```
pop() → removes 20
```

---

### ✅ Peek / Top

Shows the top element without removing it.

```
peek() → 10
```

---

### ✅ isEmpty()

Checks whether the stack is empty.

```
Returns True or False
```

---

## 📦 3. Array Implementation of Stack

### 🧠 Concept

* Stack can be implemented using an array or list.
* The last index represents the top of the stack.

### ⭐ Python Implementation

```python
stack = []

# Push operation
stack.append(10)
stack.append(20)

# Pop operation
stack.pop()

# Peek operation
print(stack[-1])
```

### ✅ Advantages

* Easy to implement
* Fast operations

### ❌ Disadvantages

* Fixed size in static arrays
* Possible overflow

---

## 🔗 4. Linked List Implementation of Stack

### 🧠 Concept

* Stack is implemented using nodes.
* Each node stores data and reference to next node.
* Top pointer represents the top element.

### ⭐ Python Implementation

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.top is None:
            return "Stack is Empty"
        temp = self.top
        self.top = self.top.next
        return temp.data
```

### ✅ Advantages

* Dynamic size
* No overflow (until memory is full)

### ❌ Disadvantages

* Extra memory required for pointers

---

## 🚀 5. Applications of Stack

### ⭐ Function Calls / Recursion

* Programming languages use stack to manage function calls.

### ⭐ Undo / Redo Operations

* Text editors
* Photoshop
* MS Word

### ⭐ Expression Evaluation

* Used in compilers and calculators.

### ⭐ Parenthesis Checking

```
{[()]} → Valid
```

### ⭐ Browser History

* Back and forward navigation.

---

## 💻 6. Practice Problems

### 🟢 Easy

* Implement stack using array
* Implement stack using linked list
* Valid parentheses problem

### 🟡 Medium

* Next greater element
* Min stack
* Reverse a string using stack

### 🔴 Hard / Interview Level

* Evaluate postfix expression
* Stock span problem

---

## 🎯 Quick Revision

| Topic        | Key Idea                 |
| ------------ | ------------------------ |
| Stack        | LIFO data structure      |
| Push         | Add element to top       |
| Pop          | Remove top element       |
| Peek         | View top element         |
| Array Stack  | Uses list/array          |
| Linked Stack | Uses nodes               |
| Applications | Recursion, Undo, Browser |

---

✅ **Conclusion:**
Stack is a simple but powerful data structure widely used in programming, memory management, and problem solving.
