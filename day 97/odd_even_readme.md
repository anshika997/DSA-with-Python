# Odd Even Linked List - Detailed Explanation

## Problem
Rearrange a linked list so that odd indexed nodes come first, followed by even indexed nodes.

## Code
class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head 

        odd = head 
        even = even_head = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next 

            even.next = odd.next 
            even = even.next

        odd.next = even_head
        return head

## Dry Run
Input: 1→2→3→4→5  
Output: 1→3→5→2→4

## Complexity
Time: O(n)  
Space: O(1)
