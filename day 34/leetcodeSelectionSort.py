class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n):
            mn = nums[i]
            ind = i 
            for j in range(i+1,n):
                if nums[j]<mn:
                    mn = nums[j]
                    ind = j 
            temp = nums[i]
            nums[i]=nums[ind]
            nums[ind]=temp
        return nums
sol = Solution ()
print(sol.sortArray([5,2,3,1]))