class Solution:
    def search(self, nums, target):
        n = len(nums)
        for i in range(n):
            if target in nums :
                return True 
            else:
                return False
print(Solution().search([-1,0,3,5,9,12], 9))
print(Solution().search([-1,0,3,5,9,12], 2))