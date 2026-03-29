class Solution:
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        count = 0
        max_count = 0 
        for i in range (0,n):
            if nums[i] == 1:
                count += 1 
            else:
                max_count = max(count,max_count)
                count = 0 
        return max(count,max_count) 
Solution=Solution()
print(Solution.findMaxConsecutiveOnes([1,1,0,1,1,1])) # Output: 3