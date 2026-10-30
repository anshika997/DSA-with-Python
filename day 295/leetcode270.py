
# Definition of Linked List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):

        store = []
        riverse = []

        curr = head

        # Step 1: Store linked list values
        while curr:
            store.append(curr.val)
            curr = curr.next

        # Step 2: Reverse left to right portion
        riverse = store[left - 1:right][::-1]

        # Step 3: Replace original portion
        store[left - 1:right] = riverse

        # Step 4: Create a new linked list
        new_node = ListNode(0)
        curr = new_node

        for value in store:
            curr.next = ListNode(value)
            curr = curr.next

        return new_node.next


# Function to create linked list
def create_linked_list(values):
    dummy = ListNode(0)
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next


# Function to print linked list
def print_linked_list(head):
    curr = head

    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next

    print("None")


# Main Program
if __name__ == "__main__":

    solution = Solution()

    # Test Case 1
    values = [1, 2, 3, 4, 5]
    left = 2
    right = 4

    head = create_linked_list(values)

    print("Original Linked List:")
    print_linked_list(head)

    result = solution.reverseBetween(head, left, right)

    print("After Reversing:")
    print_linked_list(result)

    # Test Case 2
    values = [5]
    left = 1
    right = 1

    head = create_linked_list(values)

    print("\nTest Case 2:")
    result = solution.reverseBetween(head, left, right)
    print_linked_list(result)
