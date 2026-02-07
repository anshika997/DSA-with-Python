# how we make a linked list 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
# create a object named as a of class Node and pass a value 5 on that and by default the next is none
a = Node(5)
b = Node(3)
c = Node(7)
a.next=b
b.next=c

head = a 
print(head.data)
print(head.next.data)
print(head.next.next.data)


#traverse linkedlist
def printLinkedList(head):
    curr = head 
    while curr!=None:
        print(curr.data,end=" ")
        curr = curr.next
print("\ntraverse linkedlist\n")
printLinkedList(head)

# insertion at the beginning of the node 
newNode=Node(4)
newNode.next=head
head = newNode
print("\ninsertion at the beginning of the node\n")
printLinkedList(head)

# insertion at the end of the node 

newNode = Node(1)
curr = head 
while curr.next != None:
    curr = curr.next
curr.next=newNode
print("\ninsertion at the end of the node\n")
printLinkedList(head)

# insertion at the kth index of the node 
k = 2
newNode = Node(6)
curr = head 
for i in range(k-1):
    curr = curr.next
newNode.next= curr.next
curr.next=newNode
print("\ninsertion at the kth index of the node\n")
printLinkedList(head)

# deletion of the node at the beginning
head = head.next
print("\ndeleting the first node\n")

printLinkedList(head)


# deleting the last node 

curr = head 
while curr.next.next!=None:
    curr = curr.next
curr.next = None
print("\ndeleting the last node\n ")
printLinkedList(head)

# deleting the kth node 

k= 2
curr = head 
for i in range(k-1):
    curr = curr.next
curr.next = curr.next.next
print("\ndeleting the kth node\n ")
printLinkedList(head)
print("\n")

# how we make a Doubly linked list 
class DoublyNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

a = Node(5)
b = Node(3)
c = Node(7)

a.next=b
b.prev=a
b.next=c
head = a 

print(head.data)
print(head.next.data)
print(head.next.next.data)

#circular linked list


# how we make a circular linked list 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
a = Node(5)
b = Node(3)
c = Node(7)

a.next=b
b.next=c
c.next=a

head = a 
print(head.data)
print(head.next.data)
print(head.next.next.data)

curr = head 
while True:
    print(curr.data,end=" ")
    curr = curr.next
    if curr==head:
        break