import heapq
class Solution:
    def lastStoneWeight(self, stones,k):
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap)>1:

            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            diff = a-b 
            if diff!=0:
                heapq.heappush(heap,-diff)
        if len(heap)==0:
            return 0
        else:
            return -heapq.nlargest(k,heap)[-1]
object = Solution()

print(object.lastStoneWeight(([3,2,1,5,6,4]), 3)) # o