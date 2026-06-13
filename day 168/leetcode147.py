class Solution:
    def minDays(self, bloomDay, m, k):
        n = len(bloomDay) 
        if (k*m)>n:
            return -1
        l = min(bloomDay)
        r = max(bloomDay)
        while l < r:
            mid = (l+r)//2
            bouq = 0 
            flow = 0
            for day in bloomDay:
                if day <= mid :
                    flow += 1
                    if flow == k :
                        bouq +=1
                        flow = 0 
                else :
                    flow = 0 
            if bouq >= m :
                r = mid 
            else :
                l = mid+1
        return l
print(Solution().minDays([1,10,3,10,2], 3, 1))
print(Solution().minDays([1,10,3,10,2], 3, 2))
print(Solution().minDays([7,7,7,7,12,7,7], 2, 3))
print(Solution().minDays([1000000000,1000000000], 1, 1))

        
         


