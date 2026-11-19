class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        return s == s[::-1]
Solution= Solution()
print(Solution.isPalindrome("A man, a plan, a canal: Panama"))