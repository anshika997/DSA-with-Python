class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t= sorted(t)
        return s==t
Solution = Solution()
print(Solution.isAnagram("anagram","nagaram"))