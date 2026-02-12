class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# -------- MAIN (VS Code run) --------
if __name__ == "__main__":
    # Create nodes
    head = ListNode(3)
    second = ListNode(2)
    third = ListNode(0)
    fourth = ListNode(-4)

    # Connect nodes
    head.next = second
    second.next = third
    third.next = fourth

    # Create cycle: last node pointing to second node
    fourth.next = second

    sol = Solution()
    print("Cycle present:", sol.hasCycle(head))