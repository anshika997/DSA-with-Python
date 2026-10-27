
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA, headB):
        # Step 1: Find lengths
        lenA = 0
        lenB = 0

        temp = headA
        while temp:
            lenA += 1
            temp = temp.next

        temp = headB
        while temp:
            lenB += 1
            temp = temp.next

        # Step 2: Initialize pointers
        currA = headA
        currB = headB

        # Step 3: Align both lists
        while lenA > lenB:
            currA = currA.next
            lenA -= 1

        while lenB > lenA:
            currB = currB.next
            lenB -= 1

        # Step 4: Find intersection
        while currA is not currB:
            currA = currA.next
            currB = currB.next

        return currA


# Helper function to print a linked list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Create common part: 8 -> 4 -> 5
common = ListNode(8)
common.next = ListNode(4)
common.next.next = ListNode(5)

# List A: 4 -> 1 -> 8 -> 4 -> 5
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = common

# List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = common

# Solve
solution = Solution()
result = solution.getIntersectionNode(headA, headB)

if result:
    print("Intersection Node:", result.val)
else:
    print("No Intersection")

