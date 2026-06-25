class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):

        if head is None or head.next is None:
            return head

        temp = head
        count = 0

        # Count total nodes
        while temp is not None:
            count += 1
            temp = temp.next

        # Find middle
        mid = count // 2

        temp = head

        while mid > 0:
            temp = temp.next
            mid -= 1

        return temp


# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
middle = sol.middleNode(head)

print("Middle Node:", middle.val)