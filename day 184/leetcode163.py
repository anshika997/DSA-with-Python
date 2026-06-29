# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        if head is None or head.next is None :
            return head
        newHead = self.reverseList(head.next)

        front = head.next
        front.next = head  
        head.next = None 
        return newHead
Solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print("Original List:")
curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")
print("Reversed List:")
new_head = Solution.reverseList(head)
curr = new_head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")
