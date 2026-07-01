# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        slow = head 
        fast = head
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next
            if slow == fast :
                return True 
        return False 
Solution = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # Create a cycle
print("Does the linked list have a cycle?", Solution.hasCycle(head))  # Output: True
print("Does the linked list have a cycle?", Solution.hasCycle(None))  # Output: False