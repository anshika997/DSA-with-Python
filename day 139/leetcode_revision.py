class Solution:
    def removeElement(self, nums , val):
        valid = []

        for x in nums:
            if x != val:
                valid += [x]

        nums[:] = valid

        return len(valid)
Solution = Solution()
print(Solution.removeElement([3, 2, 2, 3], 3    ))
print(Solution.removeElement([0, 1, 2, 2, 3 , 0, 4, 2] , 2))