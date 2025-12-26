class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums) 
        start = 0 
        
        for i in range(1,n):
            if nums[i]!=nums[start]:
                start+=1 
                nums[start]=nums[i] 
        return start+1
    
sol=Solution()
print(sol.removeDuplicates([1,1,1,1,2,2,2,3,4,5]))