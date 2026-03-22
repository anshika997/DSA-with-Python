import heapq
class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]
object = Solution()
print(object.findKthLargest([3,2,1,5,6,4],2))  # Output: 5