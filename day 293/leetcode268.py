
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        tail = dummy

        currA = list1
        currB = list2

        while currA is not None and currB is not None:
            if currA.val <= currB.val:
                tail.next = currA
                currA = currA.next
            else:
                tail.next = currB
                currB = currB.next

            tail = tail.next

        # Attach remaining nodes
        if currA is not None:
            tail.next = currA
        else:
            tail.next = currB

        return dummy.next


# Helper function to create a linked list
def create_list(values):
    dummy = ListNode(-1)
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


# Helper function to print a linked list
def print_list(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# Test case
list1 = create_list([1, 2, 4])
list2 = create_list([1, 3, 4])

solution = Solution()
merged = solution.mergeTwoLists(list1, list2)

print("Merged Linked List:")
print_list(merged)
