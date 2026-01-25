# upper bound implementation
class Solution:
        def upperBound(self,nums,target):
            n = len(nums)
            l = 0 
            r = n-1
            ans = n
            while l <= r:
                mid =(l+r)//2
                if nums[mid] > target:
                    ans = mid
                    r = mid - 1
                else :
                    l = mid+1
            return ans 
        def searchInsert(self, nums: list[int], target: int) -> int:
            return self.upperBound(nums,target)
sol = Solution()
print(sol.searchInsert([1,3,5,6], 5)) 

