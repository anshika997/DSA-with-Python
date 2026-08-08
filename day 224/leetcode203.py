class Solution:
    def sortSentence(self, s) :

        words = s.split()

        ans = [""] * len(words)

        for word in words:

            pos = int(word[-1])

            actual_word = word[:-1]

            ans[pos - 1] = actual_word

        return " ".join(ans)
Solution = Solution()
print(Solution.sortSentence('this1 work4 is2 the3'))