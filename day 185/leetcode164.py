# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head): 
        temp = head 
        check = {}
        while temp is not None :
            if temp in check :
                return True 
            check[temp] = 1
            temp = temp.next
        return False
Solution = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # Create a cycle
print("Does the linked list have a cycle?", Solution.hasCycle(head))  # Output: True

        