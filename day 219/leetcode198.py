class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        return "".join(word1) == "".join(word2)
Solution = Solution()
print(Solution.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
print(Solution.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))
print(Solution.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
