class Solution:
    def detectCapitalUse(self, word):
        if word.isupper():
            return True 
        elif word.islower():
            return True 
        elif word.istitle():
            return True 
        else :
            return False
Solution = Solution()
print(Solution.detectCapitalUse("USA"))  # Output: True
print(Solution.detectCapitalUse("leetcode"))  # Output: True
print(Solution.detectCapitalUse("Google"))  # Output: True
print(Solution.detectCapitalUse("FlaG"))  # Output: False