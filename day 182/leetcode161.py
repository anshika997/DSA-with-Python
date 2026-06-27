class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        stack = []
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next
        temp = head
        while temp:
            temp.val = stack.pop()
            temp = temp.next
        return head
Solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(Solution.reverseList(head).val)  # Output: 5