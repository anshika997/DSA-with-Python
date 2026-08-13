class Solution:
    def mergeAlternately(self, word1, word2) :
        combined = word1 + word2
        result = []

        min_len = min(len(word1), len(word2))

        for i in range(min_len):
            result.append(combined[i])
            result.append(combined[len(word1) + i])

        if len(word1) > len(word2):
            result.extend(word1[min_len:])
        else:
            result.extend(word2[min_len:])

        return "".join(result)
Solution = Solution()
print(Solution.mergeAlternately('abc','pqr'))