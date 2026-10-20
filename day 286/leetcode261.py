class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        middle = head 
        double  = head 
        while double and double.next and middle :
            middle = middle.next
            double = double.next.next 
        return middle 
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Find the middle node
solution = Solution()
result = solution.middleNode(head)

print(result.val)