"""
        This function returns the length of the last word in a string.

        Approach:
        - First, strip() is used to remove trailing and leading spaces.
        - Then we traverse the string from the end using negative indexing.
        - We keep moving left until a space is found.
        - The number of characters crossed gives the length of the last word.

        Example:
        Input  : "hello anshika "
        After strip : "hello anshika"
        Last word   : "anshika"
        Output : 7

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        n = len(s)
        i=-1
        while i>=(-1*n) and s[i]!=" ":
            i-=1
        i+=1
        i*=-1
        return i 
sol=Solution()
print(sol.lengthOfLastWord("hello anshika "))

#another way to solve 

"""
        This function calculates the length of the last word in a string.

        Approach:
        - Remove leading and trailing spaces using strip().
        - Traverse the string from right to left.
        - Count characters until a space is encountered.
        - Stop as soon as the first space after the last word is found.

        Example:
        Input  : " hello world "
        After strip : "hello world"
        Last word   : "world"
        Output : 5

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        c=0
        for i in range(len(s) -1,-1,-1):
            if s[i]!=" ":
                c+=1
            else :
                s[i]==" "
                break
        return c 
sol=Solution()
print(sol.lengthOfLastWord(" hello world "))