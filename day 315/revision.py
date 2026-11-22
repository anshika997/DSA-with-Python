class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = ""
        freq1 = {}
        for i in s:
            if i not in freq1 :
                freq1[i] = 1
            else :
                freq1[i] += 1
        freq2 = {}
        for i in t:
            if i not in freq2 :
                freq2[i] = 1
            else :
                freq2[i] += 1
        for i in freq2:
            if i not in freq1:
                return i
            elif freq2[i] > freq1[i]:
                return i
Solution = Solution()
print(Solution.findTheDifference("abcd","abcde"))