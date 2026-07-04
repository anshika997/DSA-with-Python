# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        stack = []
        temp = head 
        while temp is not None :
            stack.append(temp.val)
            temp = temp.next
        temp = head 
        while temp is not None :
            if temp.val != stack.pop():
                return False
            temp = temp.next 
        return True 
Solution = Solution ()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print(Solution.isPalindrome(head))  # Output: True
