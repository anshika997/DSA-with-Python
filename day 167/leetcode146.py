class Solution:
    def minEatingSpeed(self, piles, h):
        l = 1
        r = max(piles)

        while l < r:
            mid = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid   # ceil(pile/mid)

            if hours <= h:
                r = mid
            else:
                l = mid + 1

        return l
print(Solution().minEatingSpeed([3,6,7,11], 8))
print(Solution().minEatingSpeed([30,11,23,4,20], 5))
print(Solution().minEatingSpeed([30,11,23,4,20], 6))