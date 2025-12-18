class Solution:
    def smallerNumberThanCurrent(self,nums):
        result = []
        for i in range(len(nums)):
            count =0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            result.append(count)
        return result
sol = Solution()
print(sol.smallerNumberThanCurrent([8,1,2,2,3]))