class Solution:
    def removeElement(self, nums, val):
        write = 0

        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1

        return write
Solution = Solution()
print(Solution.removeElement([3, 2, 2, 3], 3    ))
print(Solution.removeElement([0, 1, 2, 2, 3 , 0, 4, 2] , 2))