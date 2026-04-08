class Solution:
    def canJump(self, nums):
        n = len(nums)
        max_index = 0
        for i in range(0,n):
            if i > max_index :
                return False 
            max_index = max(max_index,i+nums[i])
        return True 
        
Solution = Solution()
print(Solution.canJump([2,3,1,1,4]))  # Output: True
print(Solution.canJump([3,2,1,0,4]))  # Output: False
