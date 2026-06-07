class Solution:
    def singleNonDuplicate(self, nums):
        n = len(nums)
        ans = 0 
        for i in range(n):
            ans ^= nums[i]
        return ans
print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(Solution().singleNonDuplicate([3,3,7,7,10,11,11]))