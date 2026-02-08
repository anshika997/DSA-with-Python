class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        p1 = head
        p2 = head

        # move p2 n steps ahead
        for _ in range(n):
            p2 = p2.next

        # if head is to be deleted
        if p2 is None:
            return head.next

        # move both pointers
        while p2.next is not None:
            p2 = p2.next
            p1 = p1.next

        # delete node
        p1.next = p1.next.next
        return head


# -------- Print Linked List --------
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# -------- MAIN --------
if __name__ == "__main__":
    # Create list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original List:")
    printList(head)

    n = 2
    sol = Solution()
    head = sol.removeNthFromEnd(head, n)

    print("\nAfter removing {}th node from end:".format(n))
    printList(head)