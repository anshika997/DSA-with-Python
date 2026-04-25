class Solution:
    def twoSum(self, nums,target):
        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]

            seen[nums[i]] = i
Solution = Solution()
print(Solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(Solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(Solution.twoSum([3, 3], 6))          # Output: [0, 1]