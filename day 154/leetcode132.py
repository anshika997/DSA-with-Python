class Solution:
    def search(self, nums , target):
        n = len(nums)
        l = 0 
        r = n-1
        while l <= r :
            if nums[l] == target:
                return l
            
            if nums[r] == target:
                return r
            l+=1
            r-=1
        
        return -1
print(Solution().search([-1,0,3,5,9,12], 9))
print(Solution().search([-1,0,3,5,9,12], 2))