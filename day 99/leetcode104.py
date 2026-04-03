class Solution:
    def maxScore(self, nums,k):
        n = len(nums)
        if n == k:
            return sum(nums)

        left_sum = 0
        right_sum = 0

        # take k elements from left
        for i in range(0, k):
            left_sum += nums[i]

        maxi = left_sum
        right_ind = n - 1

        # shift window
        for i in range(k-1, -1, -1):
            left_sum -= nums[i]
            right_sum += nums[right_ind]

            maxi = max(maxi, left_sum + right_sum)
            right_ind -= 1

        return maxi
Solution = Solution()
print(Solution.maxScore([1,2,3,4,5,6,1], 3))