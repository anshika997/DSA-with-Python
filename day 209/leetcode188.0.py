class Solution:
    def detectCapitalUse(self, word):

        # Case 1: All Uppercase
        allUpper = True
        for ch in word:
            if not (65 <= ord(ch) <= 90):
                allUpper = False
                break

        if allUpper:
            return True

        # Case 2: All Lowercase
        allLower = True
        for ch in word:
            if not (97 <= ord(ch) <= 122):
                allLower = False
                break

        if allLower:
            return True

        # Case 3: First Uppercase, Rest Lowercase
        if 65 <= ord(word[0]) <= 90:

            for i in range(1, len(word)):
                if not (97 <= ord(word[i]) <= 122):
                    return False

            return True

        return False
Solution = Solution()
print(Solution.detectCapitalUse("USA"))  # Output: True
print(Solution.detectCapitalUse("leetcode"))  # Output: True
print(Solution.detectCapitalUse("Google"))  # Output: True
print(Solution.detectCapitalUse("FlaG"))  # Output: False