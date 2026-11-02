
# Definition of Linked List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head):

        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                # Step 2: Reset slow to head
                slow = head

                # Step 3: Find cycle starting node
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None


# Function to create linked list with cycle
def create_linked_list(values, pos):

    if not values:
        return None

    head = ListNode(values[0])
    curr = head

    cycle_node = None
    index = 0

    for value in values[1:]:
        curr.next = ListNode(value)
        curr = curr.next
        index += 1

        if index == pos:
            cycle_node = curr

    # Connect last node to cycle starting node
    if pos == 0:
        cycle_node = head

    if pos != -1:
        curr.next = cycle_node

    return head


# Main Program
if __name__ == "__main__":

    solution = Solution()

    # Test Case 1: Cycle starts at index 1
    head = create_linked_list([3, 2, 0, -4], 1)

    result = solution.detectCycle(head)

    if result:
        print("Cycle starts at node:", result.val)
    else:
        print("No cycle")

    # Test Case 2: No cycle
    head = create_linked_list([1, 2, 3, 4], -1)

    result = solution.detectCycle(head)

    if result:
        print("Cycle starts at node:", result.val)
    else:
        print("No cycle")

    # Test Case 3: Cycle starts at head
    head = create_linked_list([1, 2], 0)

    result = solution.detectCycle(head)

    if result:
        print("Cycle starts at node:", result.val)
    else:
        print("No cycle")
