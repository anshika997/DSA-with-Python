# detect_cycle.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        hasCycle = False

        # Step 1: detect cycle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                hasCycle = True
                break

        if not hasCycle:
            return None

        # Step 2: find cycle length
        l = 1
        fast = fast.next
        while slow != fast:
            fast = fast.next
            l += 1

        # Step 3: find start of cycle
        slow = head
        fast = head

        for i in range(l):
            fast = fast.next

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


def printList(head, limit=10):
    count = 0
    while head and count < limit:
        print(head.val, end=" -> ")
        head = head.next
        count += 1
    print("...")


# -------- MAIN --------
if __name__ == "__main__":

    # Linked List create kar rahe
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # cycle bana rahe → 5 ka next 3 pe point karega
    head.next.next.next.next.next = head.next.next

    print("Linked List (cycle show nahi hota full):")
    printList(head)

    sol = Solution()
    cycle_node = sol.detectCycle(head)

    if cycle_node:
        print("Cycle starts at node value:", cycle_node.val)
    else:
        print("No Cycle")