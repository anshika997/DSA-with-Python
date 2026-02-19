# Queue using 2 stacks (VS Code runnable version)

class MyQueue:

    def __init__(self):
        self.stack1 = []   # push ke liye
        self.stack2 = []   # pop / peek ke liye

    # add element in queue
    def push(self, x):
        self.stack1.append(x)

    # remove element from queue
    def pop(self):
        self.peek()   # ensure stack2 has elements
        return self.stack2.pop()

    # get front element
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    # check if queue empty
    def empty(self):
        return not self.stack1 and not self.stack2


# ===== MAIN (so it runs in VS Code) =====
if __name__ == "__main__":

    q = MyQueue()

    print("Push 10, 20, 30")
    q.push(10)
    q.push(20)
    q.push(30)

    print("Front element:", q.peek())   # 10

    print("Pop:", q.pop())              # 10
    print("Pop:", q.pop())              # 20

    print("Is empty?", q.empty())       # False

    print("Pop:", q.pop())              # 30
    print("Is empty?", q.empty())       # True