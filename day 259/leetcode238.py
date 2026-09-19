class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        l = 0
        maxx = window_sum
        while l+k < len(nums):
            window_sum = window_sum - nums[l] + nums[k+l]
            maxx = max(window_sum,maxx)
            l+=1
        return maxx/k
Solution = Solution()
print(Solution.findMaxAverage([1,12,-5,-6,50,3],4))