
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:

        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head


# Create Linked List
def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    curr = head

    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


# Print Linked List
def print_linked_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    print(values)


# Test Cases
solution = Solution()

test_cases = [
    [2, 1],
    [1, 3, 4, 7, 1, 2, 6],
    [1, 2, 3, 4],
    [1]
]

for values in test_cases:
    head = create_linked_list(values)

    print("Input: ", values)

    result = solution.deleteMiddle(head)

    print("Output:", end=" ")
    print_linked_list(result)
    print()
