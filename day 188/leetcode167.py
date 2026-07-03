# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        temp = head 
        result = set()
        while temp is not None and temp.next is not None :
            if temp  in result :
                return temp 
            result.add(temp)
            temp = temp.next
        return None 
Solution = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # Create a cycle
print (f"Cycle starts at node with value: {Solution.detectCycle(head).val}")
