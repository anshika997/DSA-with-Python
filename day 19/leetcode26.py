"""
        This function reverses the order of words in a given string.

        Steps:
        1. strip() removes leading and trailing spaces from the string.
        2. split() converts the string into a list of words.
        3. reverse() reverses the list of words in-place.
        4. join() combines the reversed words using a single space.

        Example:
        Input  : "the sky is blue"
        Output : "blue is sky the"

        Time Complexity: O(n)
        Space Complexity: O(n)

"""

class Solution:
    def reverseWords(self, s: str) -> str: 
        s=s.strip()
        s=s.split()
        s.reverse()
        return " ".join(s)
sol = Solution()
print(sol.reverseWords("the sky is blue"))



# or we can also solve this like that 
class Solution:
    def reverseWords(self, s: str) -> str: 
        s=s.strip().split()
        # s=s.split()
        s.reverse()
        return " ".join(s)
sol = Solution()
print(sol.reverseWords("the sky is blue"))