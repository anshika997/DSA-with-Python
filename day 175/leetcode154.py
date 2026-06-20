class Solution:
    def rotateString(self, s, goal):
        n = len(s)
        m = len(goal)
        if n != m :
            return False
        result = s + s
        return goal in result  
print(Solution().rotateString("abcde", "cdeab"))
print(Solution().rotateString("abcde", "abced"))