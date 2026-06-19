class Solution:
    def rotateString(self, s,goal):
        n = len(s)
        m = len(goal)
        if n!=m:
            return False 
        for i in range(0,n):
            result = s[i:] + s[:i]  
            if result == goal :
                return True 
        return False 
print(Solution().rotateString("abcde", "cdeab"))
print(Solution().rotateString("abcde", "abced"))