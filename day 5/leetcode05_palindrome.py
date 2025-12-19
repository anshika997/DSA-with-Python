"""
Day 5: Digit-Based Problems (LeetCode Practice)
--------------------------------------------------
Problem 2: Palindrome Number
--------------------------------------------------
Logic:
- Store the original number
- Reverse the number using modulo and integer division
- Compare the reversed number with the original
- If both are equal, the number is a palindrome

Time Complexity: O(d)
Space Complexity: O(1)
(where d is the number of digits)

--------------------------------------------------
Summary:
- Both problems are solved using digit extraction
- No strings or extra data structures used
- Efficient and optimized for large numbers
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        while temp > 0:
            r= temp % 10
            temp//=10
            rev = rev*10+r
        return rev==x
sol=Solution()
print(sol.isPalindrome(121))