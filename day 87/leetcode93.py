import heapq
class Solution:
    def lastStoneWeight(self, stones):
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
            return -heap[0]
object = Solution()
print(object.lastStoneWeight(([2,7,4,1,8,1])))  # Output: 1
        