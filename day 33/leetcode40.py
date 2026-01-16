class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val :
                nums.pop(i)
            else:
                i+=1
        return len(nums)
sol = Solution()
print(sol.removeElement([3,4,5,6,7,3],3))
            