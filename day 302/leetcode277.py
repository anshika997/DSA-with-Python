class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1, a, b, list2):

        # Step 1: a-1 index par pahucho
        prev = list1

        for i in range(a - 1):
            prev = prev.next

        # Step 2: b+1 index par pahucho
        after = prev

        for i in range(b - a + 2):
            after = after.next

        # Step 3: list2 ka last node find karo
        tail = list2

        while tail.next:
            tail = tail.next

        # Step 4: Dono lists connect karo
        prev.next = list2
        tail.next = after

        return list1


# Create Linked List
def createList(arr):
    dummy = ListNode()
    curr = dummy

    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next

    return dummy.next


# Print Linked List
def printList(head):
    curr = head

    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next

    print("None")


# Main
list1 = createList([0, 1, 2, 3, 4, 5])
list2 = createList([100, 101, 102])

a = 2
b = 4

obj = Solution()
result = obj.mergeInBetween(list1, a, b, list2)

print("Final Linked List:")
printList(result)