class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        curr = head
        for _ in range(length // 2):
            curr = curr.next

        return curr


# -------- RUN HERE --------

# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
mid = sol.middleNode(head)

print(mid.val)
