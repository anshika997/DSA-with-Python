class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


# Create linked list: 4 -> 5 -> 1 -> 9
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

# Node to delete (5)
node = head.next

# Delete node
sol = Solution()
sol.deleteNode(node)

# Print linked list
curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next

print("None")