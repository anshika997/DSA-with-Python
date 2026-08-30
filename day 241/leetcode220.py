class Solution:
    def maxProduct(self, nums):
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                result.append((nums[i]-1)*(nums[j]-1))
        return max(result)
Solution = Solution()
print(Solution.maxProduct([3,4,5,2]))
print(Solution.maxProduct([1,5,4,5]))
