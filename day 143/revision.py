class Solution:
    def removeElement(self, nums, val):
        result = []

        for i in range(len(nums)):
            if nums[i] != val:
                result.append(nums[i])

        nums[:len(result)] = result

        return len(result)
Solution = Solution()
print(Solution.removeElement([3, 2, 2, 3], 3    ))
print(Solution.removeElement([0, 1, 2, 2, 3 , 0, 4, 2] , 2))