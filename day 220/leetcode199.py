class Solution:
    def mostWordsFound(self, sentences):
        # s = sentences.split()
        maxx = 0
        for sentence in sentences :
            word = sentence.split()
            if len(word)> maxx:
                maxx = len(word)
        return maxx 
Solution = Solution()
print(Solution.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
print(Solution.mostWordsFound(["please wait", "continue to fight", "continue to win"]))