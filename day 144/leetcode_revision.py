class Solution:
    def removeElement(self, nums, val):
        pos = 0

        for element in nums:
            if element != val:
                nums[pos] = element
                pos += 1

        return pos
Solution = Solution()
print(Solution.removeElement([3, 2, 2, 3], 3    ))
print(Solution.removeElement([0, 1, 2, 2, 3 , 0, 4, 2] , 2))