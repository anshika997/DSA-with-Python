class MyStack:

    def __init__(self):
        self.q1=[]
        self.q2=[]
        
    def push(self, x: int) -> None:
        self.q2.append(x)
        while len(self.q1)>0:
            self.q2.append(self.q1.pop(0))
        self.q1,self.q2=self.q2,self.q1# swap 

    def pop(self) -> int:
        return self.q1.pop(0)   

    def top(self) -> int:
        return self.q1[0]
        

    def empty(self) -> bool:
        return len(self.q1)==0
MyStack=MyStack()
MyStack.push(1)
MyStack.push(2)
MyStack.push(3)
print(MyStack.top())
print(MyStack.pop())
print(MyStack.empty())