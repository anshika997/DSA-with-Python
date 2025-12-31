"""
PROBLEM STATEMENT:
Given a string s, determine whether it is a palindrome.
A palindrome is a string that reads the same forward and backward.
While checking:
1. Ignore all non-alphanumeric characters.
2. Comparison should be case-insensitive.

APPROACH / LOGIC:
1. Convert the string to lowercase to handle case-insensitive comparison.
2. Use the two-pointer technique:
   - One pointer (i) starts from the beginning of the string.
   - Another pointer (j) starts from the end of the string.
3. Move the left pointer forward if it points to a non-alphanumeric character.
4. Move the right pointer backward if it points to a non-alphanumeric character.
5. When both pointers point to alphanumeric characters:
   - Compare the characters.
   - If they are equal, move both pointers inward.
   - If they are not equal, return False immediately.
6. Continue this process until both pointers meet or cross.
7. If all valid characters match, return True.

WHY THIS WORKS:
- Skipping non-alphanumeric characters satisfies the problem constraints.
- Two-pointer technique allows comparison from both ends efficiently.
- No extra space is used for creating a new string.

TIME COMPLEXITY:
O(n), where n is the length of the string.
Each character is processed at most once.

SPACE COMPLEXITY:
O(1), as no extra space is used apart from a few variables.
"""
class solution:
    def isAlphanumeric(self,s):
        x=ord(s)
        if 97<=x<=122 or 67<=x<=90 or 48<=x<=57:
            return True
        return False
        
    def ispalindrom(self,s:str)->bool:
            s=s.lower()
            i=0
            j=len(s)-1
            while i<j:
                if not self.isAlphanumeric(s[i]):
                    i+=1
                elif not self.isAlphanumeric(s[j]):
                    j-=1
                elif s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True
sol = solution()
print(sol.ispalindrom("A man, a plan, a canal: Panama"))