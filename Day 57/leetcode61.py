class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head

        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# -------- MAIN --------
if __name__ == "__main__":
    # Create list with duplicates: 1 -> 1 -> 2 -> 3 -> 3 -> 4
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(4)

    print("Original List:")
    printList(head)

    sol = Solution()
    head = sol.deleteDuplicates(head)

    print("After Removing Duplicates:")
    printList(head)