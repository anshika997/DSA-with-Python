class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()
        return s
Solution = Solution()
print(Solution.reverseString(["h","e","l","l","o"]))