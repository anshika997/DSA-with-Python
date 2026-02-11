class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        p1 = headA
        p2 = headB
        c = 0

        while True:
            if p1 == p2:
                return p1

            p1 = p1.next
            p2 = p2.next

            if p2 == None:
                c += 1
                p2 = headA

            if p1 == None:
                p1 = headB

            if c > 1:
                return None


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# -------- MAIN --------
if __name__ == "__main__":

    # Common part
    common = ListNode(8)
    common.next = ListNode(10)

    # List A
    headA = ListNode(3)
    headA.next = ListNode(7)
    headA.next.next = common

    # List B
    headB = ListNode(99)
    headB.next = ListNode(1)
    headB.next.next = common

    print("List A:")
    printList(headA)

    print("List B:")
    printList(headB)

    sol = Solution()
    result = sol.getIntersectionNode(headA, headB)

    if result:
        print("Intersection at:", result.val)
    else:
        print("No Intersection")