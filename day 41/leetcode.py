# binary search
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l = 0 
        r = n-1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else :
                r = mid -1 
        return -1 
sol = Solution()
print(sol.search([-1,0,3,5,9,12], 9))  # Output: 4
