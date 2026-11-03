
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        curr = head
        num = 0

        while curr:
            num = num * 2 + curr.val
            curr = curr.next

        return num


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


# Test Cases
solution = Solution()

head1 = create_linked_list([1, 0, 1])
print("Output 1:", solution.getDecimalValue(head1))

head2 = create_linked_list([0])
print("Output 2:", solution.getDecimalValue(head2))

head3 = create_linked_list([1, 0, 0, 1])
print("Output 3:", solution.getDecimalValue(head3))
