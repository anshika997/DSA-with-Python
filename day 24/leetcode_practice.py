# this will work only when the list is shorted 

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0 
        j = len(nums)-1
        while i < j :
             if nums[i]+nums[j]==target:
                return (i,j)
                break
             elif nums[i]+nums[j]<target:
                i+=1
             else:
                j-=1
sol=Solution()
print(sol.twoSum([2,7,11,15],9))