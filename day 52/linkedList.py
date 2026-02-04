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
printLinkedList(head)

# insertion at the beginning of the node 
newNode=Node(4)
newNode.next=head
head = newNode
print("\t")
printLinkedList(head)

# insertion at the end of the node 

newNode = Node(1)
curr = head 
while curr.next != None:
    curr = curr.next
curr.next=newNode
print()
printLinkedList(head)

# insertion at the kth index of the node 
k = 2
newNode = Node(6)
curr = head 
for i in range(k-1):
    curr = curr.next
newNode.next= curr.next
curr.next=newNode
print()
printLinkedList(head)