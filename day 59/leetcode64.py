class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        if head == None or head.next == None:
            return head 

        l = 0 
        last = head 
        while last.next != None:
            last = last.next
            l += 1
        l += 1

        k = k % l
        if k == 0:
            return head 

        curr = head
        for i in range(l - k - 1):
            curr = curr.next

        last.next = head 
        head = curr.next 
        curr.next = None

        return head


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# -------- MAIN --------
if __name__ == "__main__":

    # Directly values daal diye
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    k = 2

    print("Original List:")
    printList(head)

    sol = Solution()
    new_head = sol.rotateRight(head, k)

    print("After Rotation:")
    printList(new_head)