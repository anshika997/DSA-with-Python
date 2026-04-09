class Solution:
    def jump(self, nums):
        n = len(nums)
        jumpp = 0
        left = 0 
        right = 0 

        while right <n-1:
            farthest = 0 
            for i in range(left,right+1):
                farthest = max(farthest, i+nums[i])
            left = right+1
            right = farthest
            jumpp += 1
        return jumpp
Solution = Solution()
print(Solution.jump([2,3,1,1,4]))  # Output: 2
print(Solution.jump([2,3,0,1,4]))  # Output: 2