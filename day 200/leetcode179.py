class Solution:
    def heightChecker(self, heights):
        r = sorted(heights)
        result = 0 
        for i in range(0,len(r)):
            if r[i] != heights[i]:
                result += 1 
        return result
Solution = Solution()
print(Solution.heightChecker([1,1,4,2,1,3]))
print(Solution.heightChecker([5,1,2,3,4]))
        