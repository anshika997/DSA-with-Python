
from typing import Optional


class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Linked List create karo: 3 -> 2 -> 0 -> -4
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4

# Cycle create karo: -4 -> 2
node4.next = node2

# Solution run karo
sol = Solution()
result = sol.hasCycle(node1)

print(result)
