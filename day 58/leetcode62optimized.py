# this is the optimized version of the solution, which uses O(1) space by reversing the second half of the linked list in place
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        # Step 1: find middle (slow & fast)
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: compare first half & reversed second half
        p1 = head
        p2 = prev

        while p2:   # only need to check second half
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True


# -------- MAIN (VS Code run) --------
if __name__ == "__main__":
    # Example: 1 -> 2 -> 2 -> 1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)

    sol = Solution()
    print(sol.isPalindrome(head))   # True