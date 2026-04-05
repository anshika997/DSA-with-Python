class Solution:
    def findContentChildren(self, g, s):
        n = len(g)
        m = len(s)
        g.sort()
        s.sort()
        left = 0 
        right = 0
        count = 0 
        while left<n and right<m:
            if g[left]<=s[right]:
                count += 1
                left +=1
            right +=1
        return count
            
Solution = Solution()
print(Solution.findContentChildren([1,2,3], [1,1]))  # Output: 1
print(Solution.findContentChildren([1,2], [1,2,3]))  # Output: 2
        