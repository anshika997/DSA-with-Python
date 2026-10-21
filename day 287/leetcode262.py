class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


# Create Linked List: 4 -> 5 -> 1 -> 9
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

# Delete node with value 5
node_to_delete = head.next

Solution().deleteNode(node_to_delete)

# Print Linked List
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next

print("None")