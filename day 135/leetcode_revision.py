class Solution:
    def removeElement(self, nums,val):
        k = 0

        for index, num in enumerate(nums):
            if num != val:
                nums[k] = num
                k += 1

        return k
Solution = Solution()   
print(Solution.removeElement([3, 2, 2, 3], 3 ))
print(Solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2] , 2))