
class Solution:
    def sumOfArray(self,nums:list[int])->list[int]:
        n = len(nums)
        result=[]
        result.append(nums[0])
        for i in range(1,n):
            x = result[i-1]+nums[i]
            result.append(x)
        return result
sol=Solution()
print(sol.sumOfArray([1,2,3,4,5]))

# Better time complexity
class Solution:
    def sumOfArray(self,nums:int):
        result=[]
        total = 0
        for i in nums:
            total += i
            result.append(total)
        return result
sol=Solution()
print(sol.sumOfArray([1,2,3,4,5,6,7,8]))

# in place optimized version
class solution:
    def SumOfArray(self,nums):
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
        return nums
sol=solution()
print(sol.SumOfArray([1,2,3]))
        
            
        
        