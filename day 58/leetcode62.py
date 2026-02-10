# iy is not optimized for space, but it is straightforward and easy to understand. It reverses the linked list and then compares the original and reversed lists node by node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        # save original head
        orig = head

        # reverse the list
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # compare original and reversed
        p1 = orig
        p2 = prev

        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True

def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# -------- MAIN --------
if __name__ == "__main__":
    
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    head.next.next.next.next.next = ListNode(1)

    print("Original List:")
    printList(head)

    sol = Solution()
    is_palindrome = sol.isPalindrome(head)

    print("Is Palindrome:", is_palindrome)