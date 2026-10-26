
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # Step 1: Count the length
        length = 0
        temp = head

        while temp is not None:
            length += 1
            temp = temp.next

        # Step 2: Find target index
        index = length - n

        # Step 3: If head needs to be deleted
        if index == 0:
            return head.next

        # Step 4: Reach the node before target
        curr = head
        count = 0

        while count < index - 1:
            curr = curr.next
            count += 1

        # Step 5: Delete the target node
        curr.next = curr.next.next

        return head


def print_list(head):
    while head is not None:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n = 2

solution = Solution()
head = solution.removeNthFromEnd(head, n)

print("Updated Linked List:")
print_list(head)
