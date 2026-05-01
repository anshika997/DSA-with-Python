class Solution:
    def removeElement(self, nums,val):
        count = nums.count(val)   # count how many to remove
        
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        
        return k
Solution = Solution()
print(Solution.removeElement([3, 2, 2, 3], 3    ))
print(Solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))  