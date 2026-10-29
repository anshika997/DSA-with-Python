
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        curr = head
        values = []

        # Store all node values
        while curr is not None:
            values.append(curr.val)
            curr = curr.next

        # Compare original list with reversed list
        return values == values[::-1]


# Helper function to create a linked list
def create_list(nums):
    dummy = ListNode()
    curr = dummy

    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next

    return dummy.next


# Test cases
solution = Solution()

head1 = create_list([1, 2, 2, 1])
print(solution.isPalindrome(head1))  # True

head2 = create_list([1, 2, 3])
print(solution.isPalindrome(head2))  # False

head3 = create_list([1])
print(solution.isPalindrome(head3))  # True
