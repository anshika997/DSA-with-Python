class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
        return set(alphabets).issubset(set(sentence))
Solution = Solution()
print(Solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))