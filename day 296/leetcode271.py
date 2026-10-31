
# Definition of Linked List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):

        # Step 1: Handle empty or single-node list
        if head is None or head.next is None:
            return head

        curr = head

        # Step 2: Traverse the linked list
        while curr and curr.next:

            # Step 3: Check duplicate values
            if curr.val == curr.next.val:
                curr.next = curr.next.next

            else:
                curr = curr.next

        # Step 4: Return updated linked list
        return head


# Function to create Linked List
def create_linked_list(values):
    dummy = ListNode(0)
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next


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
    values = [1, 1, 2, 3, 3]

    head = create_linked_list(values)

    print("Original Linked List:")
    print_linked_list(head)

    result = solution.deleteDuplicates(head)

    print("After Removing Duplicates:")
    print_linked_list(result)

    # Test Case 2
    values = [1, 1, 1, 2, 2, 3]

    head = create_linked_list(values)

    print("\nTest Case 2:")
    result = solution.deleteDuplicates(head)
    print_linked_list(result)

    # Test Case 3
    values = []

    head = create_linked_list(values)

    print("\nTest Case 3:")
    result = solution.deleteDuplicates(head)
    print_linked_list(result)
