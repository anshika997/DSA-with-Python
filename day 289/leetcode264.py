
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        while head is not None and head.val == val:
            head = head.next

        temp = head

        while temp is not None and temp.next is not None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head


# Linked List create karna: 1 -> 2 -> 6 -> 3 -> 6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(6)

val = 6

# Solution call karna
sol = Solution()
new_head = sol.removeElements(head, val)

# Output print karna
current = new_head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next

print("None")
