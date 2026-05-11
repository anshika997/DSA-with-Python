class Solution:
    def removeElement(self, nums, val):
        
        left = 0  # tracks position for valid elements
        
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        
        return left
Solution = Solution()
print(Solution.removeElement([3, 2, 2, 3], 3 ))
print(Solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2] , 2))