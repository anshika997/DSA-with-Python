# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head , prev = None):
        temp = head 
        prev = None
        while temp :
            front = temp.next
            temp.next = prev
            prev = temp 
            temp = front
        return prev
Solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

new_head = Solution.reverseList(head)

curr = new_head

while curr:
    print(curr.val, end=" -> ")
    curr = curr.next

print("None")