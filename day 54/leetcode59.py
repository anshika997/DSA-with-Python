class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
        
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next 

def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)
head.next.next.next.next = ListNode(2)

sol = Solution()
sol.deleteNode(head.next)   # deleting node with value 5

printList(head)