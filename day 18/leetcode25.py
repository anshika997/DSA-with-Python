"""
This function reverses the given list of characters in-place.

    Logic:
    - Use two pointers:
        i → starts from the beginning of the list
        j → starts from the end of the list
    - While i < j:
        • Swap the characters at positions i and j
        • Move i forward and j backward
    - The process continues until both pointers meet

    Time Complexity: O(n)
    Space Complexity: O(1)
"""
class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()
sol=Solution()
arr=["h","e","l","l","o"]
sol.reverseString(arr)
print(arr)