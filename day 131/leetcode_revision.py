class Solution:
    def removeElement(self, nums,val):
        filtered = list(filter(lambda x: x != val, nums))
        
        for i in range(len(filtered)):
            nums[i] = filtered[i]
        
        return len(filtered)
Solution = Solution()
print(Solution.removeElement([3, 2, 2, 3], 3 )) 
print(Solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2] , 2))