class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, x):
        self.length += 1
        newNode = Node(x)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.top is None:
            return -1

        self.length -= 1
        x = self.top.data
        self.top = self.top.next
        return x

    def getTop(self):
        if self.top is None:
            return -1
        return self.top.data

    def size(self):
        return self.length


# -------- Driver Code --------
Stack = stack()

Stack.push(1)
Stack.push(2)
Stack.push(3)
Stack.push(5)

print(Stack.getTop())   # Top element
print(Stack.size())     # Stack size
print(Stack.pop())      # Remove top
print(Stack.getTop())