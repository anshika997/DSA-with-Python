class Solution:
    def truncateSentence(self, s, k):
        word = s.split()
        sentence = []
        for i in range(k):
            sentence.append(word[i])
        return " ".join(sentence)
Solution = Solution()
print(Solution.truncateSentence("Hello how are you Contestant",4))