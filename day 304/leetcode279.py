
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
    def swapNodes(self, head, k):
        curr = head
        list1 = []

        if head is None or head.next is None:
            return head

        # Linked List values ko list mein store karo
        while curr:
            list1.append(curr.val)
            curr = curr.next

        # Dono indexes calculate karo
        i = k - 1
        j = len(list1) - k

        # Values swap karo
        list1[i], list1[j] = list1[j], list1[i]

        # Updated values Linked List mein daalo
        curr = head
        index = 0

        while curr:
            curr.val = list1[index]
            curr = curr.next
            index += 1

        return head


# Test cases
solution = Solution()

head = create_linked_list([1, 2, 3, 4, 5])
result = solution.swapNodes(head, 2)

print("Output 1:")
print_linked_list(result)


head = create_linked_list([7, 9, 6, 6, 7, 8, 3, 0, 9, 5])
result = solution.swapNodes(head, 5)

print("Output 2:")
print_linked_list(result)


head = create_linked_list([1, 2])
result = solution.swapNodes(head, 1)

print("Output 3:")
print_linked_list(result)
