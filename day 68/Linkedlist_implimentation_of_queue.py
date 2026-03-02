class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.lenght=0
    def push(self,x):
        self.lenght+=1
        newNode=Node(x)
        if self.front ==None:
            self.front =newNode
            self.rear =newNode
        else:
            self.rear.next=newNode
            self.rear=newNode
    def pop(self):
        if self.front is None:
            return -1
        x = self.front.data
        self.front = self.front.next
        self.lenght-=1
        if self.front is None:
            self.rear=None
        
        return x
    def getfront(self):
        if self.front is None:
            return -1 
        return self.front.data
    def getsize(self):
        return self.lenght

Queue = Queue()
Queue.push(5)
Queue.push(1)
Queue.push(2)
Queue.push(3)
Queue.push(4)

print(Queue.getfront())
Queue.pop()
print(Queue.getfront())
Queue.pop()
print(Queue.getfront())
print(Queue.getsize())
