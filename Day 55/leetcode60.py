class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n ):
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next
            
        if n == length:
            return head.next

        curr = head 
        for i in range (length-n-1):
            curr = curr.next
        curr.next=curr.next.next
        return head
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
sol = Solution()
new_head = sol.removeNthFromEnd(head, 2)

# print linked list
temp = new_head
while temp:
    print(temp.val, end=" -> ")
    temp = temp.next
