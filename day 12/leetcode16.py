class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        start = 1
        for i in range(2, n):
            if nums[i] != nums[start-1]:
                start += 1
                nums[start] = nums[i]

        return start + 1
sol=Solution()
print(sol.removeDuplicates([1,1,1,1,1,2,2,2,3,3,3,3,4]))