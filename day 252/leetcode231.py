import string 
class Solution:
    def modifyString(self, s):
        s = list(s) 
        for index in range(len(s)): 
            for ch in string.ascii_lowercase: 
                if s[index] == '?':
                     if (index == 0 or ch != s[index - 1]) and (index == len(s) - 1 or ch != s[index + 1]):
                        s[index] = ch
                        break 
        return "".join(s)
Solution = Solution()
print(Solution.modifyString("?zs"))