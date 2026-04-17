class Solution:
    def containsNearbyDuplicate(self, nums,k):
        window = set()
        for i in range(0,len(nums)):
            if nums[i] in window:
                return True 
            window.add(nums[i])
            if len(window)>k:
                window.remove(nums[i-k])
        return False
Solution = Solution()
print(Solution.containsNearbyDuplicate([1,2,3,1], 3)) # True
print(Solution.containsNearbyDuplicate([1,0,1,1], 1)) # True
print(Solution.containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False