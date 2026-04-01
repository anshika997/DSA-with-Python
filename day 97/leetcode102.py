class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None :
            return head 
        odd = head 
        even = even_head = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next 
            even.next = odd.next 
            even = even.next
        odd.next = even_head
        return head

Solution = Solution()
# Example usage:    

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
# Reorder the list
new_head = Solution.oddEvenList(head)
# Print the reordered list
print("Reordered list:")
current = new_head
while current:
    print(current.val, end=" ")
    current = current.next


