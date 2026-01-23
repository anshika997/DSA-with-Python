# binary search
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if  nums[i]==target:
                return i 
        return -1
sol = Solution()
print(sol.search([-1,0,3,5,9,12],9))