
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    curr = head

    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


def print_linked_list(head):
    curr = head

    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next

    print("None")


class Solution:
    def insertGreatestCommonDivisors(self, head):
        curr = head

        if head is None or head.next is None:
            return head

        while curr and curr.next:
            new_node = ListNode(math.gcd(curr.val, curr.next.val))

            new_node.next = curr.next
            curr.next = new_node

            curr = new_node.next

        return head


# Test cases
solution = Solution()

head = create_linked_list([18, 6, 10])
result = solution.insertGreatestCommonDivisors(head)

print("Test Case 1:")
print_linked_list(result)


head = create_linked_list([7])
result = solution.insertGreatestCommonDivisors(head)

print("Test Case 2:")
print_linked_list(result)


head = create_linked_list([12, 15, 18])
result = solution.insertGreatestCommonDivisors(head)

print("Test Case 3:")
print_linked_list(result)