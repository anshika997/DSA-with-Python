class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        freq = [0]*26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for ch in t:
            freq[ord(ch) - ord('a')] -=1
        for cnt in freq:
            if cnt != 0:
                return False
        return True
print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("rat", "car"))

