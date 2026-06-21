class Solution:
    def isAnagram(self, s,t):
        n = len(s)
        m = len(t)
        if n != m :
            return False 
        if sorted(s) == sorted(t) : 
            return True 
        else:
            return False
print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("rat", "car"))



        