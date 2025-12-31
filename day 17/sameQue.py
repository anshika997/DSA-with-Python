class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        return cleaned==cleaned[::-1]
sol=Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    