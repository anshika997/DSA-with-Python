class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
    
        return len(set(nums))!=len(nums)  
Solution = Solution()
print(Solution.containsDuplicate([1,2,3,1]))