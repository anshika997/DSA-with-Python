import heapq
class Solution:
    def findKthLargest(self, nums,k):
        h =[]
        for n in nums :
            heapq.heappush(h,n)
            if len(h)>k:
                heapq.heappop(h)
        return h[0]

object = Solution()
print(object.findKthLargest([3,2,1,5,6,4],2))  # Output: 5