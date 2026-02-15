class stack:
    def __init__(self):
        self.st=[]
    def push(self,x):
        self.st.append(x)
    def pop (self):
        if len(self.st)==0:
            return -1
        x = self.st[-1]
        self.st.pop()
        return x
    def top(self):
        if len(self.st)==0:
            return -1
        return self.st[-1]
    def size(self):
        return len(self.st)
Stack=stack()
Stack.push(1)
Stack.push(2)
print(Stack.top())
print(Stack.size())
print(Stack.pop())
print(Stack.top())
