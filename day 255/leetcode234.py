class Solution:
    def pivotIndex(self, nums) :
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - left - nums[i]

            if left == right:
                return i

            left += nums[i]
        return -1
Solution = Solution()
print(Solution.pivotIndex([1,7,3,6,5,6]))