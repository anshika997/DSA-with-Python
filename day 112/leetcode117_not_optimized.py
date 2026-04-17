# but this is not optimized, it is O(n^2) time complexity, we can use a hash map to optimize it to O(n) time complexity

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):   # avoid same index
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True

        return False
Solution = Solution()
print(Solution.containsNearbyDuplicate([1,2,3,1], 3)) # True
print(Solution.containsNearbyDuplicate([1,0,1,1], 1)) # True
print(Solution.containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False