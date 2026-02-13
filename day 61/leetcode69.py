# Remove Duplicates from Sorted List II (LeetCode 82)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr:
            
            # check duplicate
            if curr.next and curr.val == curr.next.val:
                
                # skip all same values
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                
                prev.next = curr.next   # remove duplicates
            
            else:
                prev = prev.next        # move prev if value unique
            
            curr = curr.next
        
        return dummy.next


# print linked list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# -------- MAIN --------
if __name__ == "__main__":

    # create sorted list
    # 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(5)

    print("Original List:")
    printList(head)

    sol = Solution()
    new_head = sol.deleteDuplicates(head)

    print("After Removing Duplicates:")
    printList(new_head)