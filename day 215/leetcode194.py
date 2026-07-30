class Solution:
    def isPrefixOfWord(self, sentence, searchWord):
        word = sentence.split()
        for i, wrd in enumerate(word):
            if wrd.startswith(searchWord):
                return i+1         
        return -1
Solution = Solution()
print(Solution.isPrefixOfWord("i love eating burger", "burg"))
print(Solution.isPrefixOfWord("this problem is an easy problem", "pro"))
print(Solution.isPrefixOfWord("hello world", "world"))