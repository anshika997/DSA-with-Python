class Solution:
    def countPairs(self, nums, k):
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range (i+1,n):
                if nums[i] == nums[j] and (i * j)%k == 0 :
                    count += 1
        return count 
Solution = Solution()
print(Solution.countPairs([3,1,2,2,2,1,3],2))