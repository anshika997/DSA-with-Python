class Solution:
    def removeOuterParentheses(self, s):
        result = ""
        level  = 0 
        for ch in s :
            if ch=="(":
                if level > 0:
                    result += ch
                level +=1   
            elif ch == ")":
                level -= 1 
                if level > 0:
                    
                    result += ch
        return result
print(Solution().removeOuterParentheses("(()())(())"))
print(Solution().removeOuterParentheses("(()())(())(()(()))"))