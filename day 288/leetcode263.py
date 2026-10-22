# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head

        while curr is not None:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node

        return prev


# Create Linked List: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


# Function to print Linked List
def print_list(head):
    while head is not None:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


print("Original Linked List:")
print_list(head)

# Reverse the Linked List
solution = Solution()
head = solution.reverseList(head)

print("Reversed Linked List:")
print_list(head)
