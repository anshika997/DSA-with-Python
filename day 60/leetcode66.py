class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        root = head
        carry = 0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            s = v1 + v2 + carry
            carry = s // 10

            head.next = ListNode(s % 10)
            head = head.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            head.next = ListNode(carry)

        return root.next


# -------- helper to print linked list --------
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# -------- MAIN (VS Code run) --------
if __name__ == "__main__":
    # Number 1: 342 → stored as 2 -> 4 -> 3
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    # Number 2: 465 → stored as 5 -> 6 -> 4
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    print("List 1:")
    printList(l1)

    print("List 2:")
    printList(l2)

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)

    print("\nResult (Sum):")
    printList(result)