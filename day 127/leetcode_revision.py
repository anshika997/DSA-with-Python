class Solution:
    def removeElement(self, nums,val):
        nums[:] = [x for x in nums if x != val]
        return len(nums)
Solution = Solution()
print(Solution.removeElement([3, 2, 2, 3], 3    ))
print(Solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))