
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    curr = head

    for value in values[1:]:
        curr.next = ListNode(value)
        curr = curr.next

    return head


def print_linked_list(head):
    curr = head
    result = []

    while curr:
        result.append(str(curr.val))
        curr = curr.next

    print(" -> ".join(result) + " -> None")


class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            # Odd position nodes ko connect karo
            odd.next = even.next
            odd = odd.next

            # Even position nodes ko connect karo
            even.next = odd.next
            even = even.next

        # Dono lists ko connect karo
        odd.next = evenHead

        return head


# Test cases
solution = Solution()

head = create_linked_list([1, 2, 3, 4, 5])
result = solution.oddEvenList(head)
print_linked_list(result)

head = create_linked_list([2, 1, 3, 5, 6, 4, 7])
result = solution.oddEvenList(head)
print_linked_list(result)

head = create_linked_list([1, 2, 3, 4])
result = solution.oddEvenList(head)
print_linked_list(result)
