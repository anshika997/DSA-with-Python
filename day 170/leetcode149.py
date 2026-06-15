class Solution:
    def reverseWords(self, s):
        result = ""
        words = s.split()
        words.reverse()
        result =" ".join(words)
        return result 
print(Solution().reverseWords("Hello World"))
print(Solution().reverseWords("  Hello   World  "))