class Solution:
    def findPeakElement(self, nums):
        n = len(nums)
        l = 0 
        r = n-1 
        while l < r:
            mid = (l+r)//2
            if nums[mid]>nums[mid+1]:
                r = mid
            else :
                l = mid+1
        return l
print(Solution().findPeakElement([1,2,3,1]))
print(Solution().findPeakElement([1,2,1,3,5,6,4]))