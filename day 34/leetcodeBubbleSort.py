class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # bubble sort 
        n = len(nums)
        for i in range (n):
            isSwap =False
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    #swap
                    temp=nums[j]
                    nums[j]=nums[j+
                    1]
                    nums[j+1]=temp
                    isSwap=True
            if not isSwap:
                break
        return nums
sol = Solution()
print(sol.sortArray([5,2,3,1]))