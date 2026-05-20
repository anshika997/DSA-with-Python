class Solution:
    def removeElement(self, nums, val):
        i = 0

        while i < len(nums):
            while i < len(nums) and nums[i] == val:
                nums.pop(i)

            i += 1

        return len(nums)
Solution = Solution()
print(Solution.removeElement([3, 2, 2, 3], 3    ))
print(Solution.removeElement([0, 1, 2, 2, 3 , 0, 4, 2] , 2))