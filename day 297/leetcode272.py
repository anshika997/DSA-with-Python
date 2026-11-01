
# Definition of Linked List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):

        # Base case
        if head is None or head.next is None:
            return head

        # Handle duplicates at starting
        while head and head.next and head.val == head.next.val:
            duplicate = head.val

            while head and head.val == duplicate:
                head = head.next

        prev = None
        curr = head

        # Traverse the linked list
        while curr and curr.next:

            if curr.val == curr.next.val:

                duplicate = curr.val

                # Skip all duplicate nodes
                while curr and curr.val == duplicate:
                    curr = curr.next

                if prev:
                    prev.next = curr

            else:
                prev = curr
                curr = curr.next

        return head


# Function to create Linked List
def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    curr = head

    for value in values[1:]:
        curr.next = ListNode(value)
        curr = curr.next

    return head


# Function to print Linked List
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
    values = [1, 2, 3, 3, 4, 4, 5]
    head = create_linked_list(values)

    print("Original Linked List:")
    print_linked_list(head)

    result = solution.deleteDuplicates(head)

    print("After Removing Duplicates:")
    print_linked_list(result)

    # Test Case 2: Duplicates at starting
    values = [1, 1, 2, 3]
    head = create_linked_list(values)

    print("\nTest Case 2:")
    result = solution.deleteDuplicates(head)
    print_linked_list(result)

    # Test Case 3: All elements duplicate
    values = [1, 1, 2, 2]
    head = create_linked_list(values)

    print("\nTest Case 3:")
    result = solution.deleteDuplicates(head)
    print_linked_list(result)

    # Test Case 4: No duplicates
    values = [1, 2, 3, 4]
    head = create_linked_list(values)

    print("\nTest Case 4:")
    result = solution.deleteDuplicates(head)
    print_linked_list(result)
