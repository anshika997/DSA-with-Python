class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Logic:
        - Traverse the string from right to left.
        - Build each word character by character.
        - When space is found, store the completed word.
        - Ignore multiple spaces.
        - Finally, manually join words with a single space.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        words = []      # list to store reversed words
        word = ""       # string to build a single word

        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                word = s[i] + word
            else:
                if word != "":
                    words.append(word)
                    word = ""

        if word != "":
            words.append(word)

        result = ""
        for i in range(len(words)):
            result += words[i]
            if i != len(words) - 1:
                result += " "

        return result


sol = Solution()
print(sol.reverseWords(" the   sky  is   blue "))
