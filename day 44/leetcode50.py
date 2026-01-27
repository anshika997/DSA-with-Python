class Solution:
    def getHours(self,piles,mid):
        ans =  0 
        for pile in piles:
            #  to find the seal value 
            ans += (pile+mid-1)//mid 
        return ans 
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)
        l = 1
        r = max(piles)
        k = r
        while l <= r:
            mid = (l+r)//2
            if self.getHours(piles,mid)>h:
                l = mid+1
            else:
                k = mid
                r = mid-1
        return k
sol= Solution()
print(sol.minEatingSpeed([3,6,7,11],8))