"""
LeetCode 121: Best Time to Buy and Sell Stock
Logic:
- min_prices keeps track of the lowest price seen so far (best day to buy).
- For each day, we calculate current profit if we sell on that day.
- Update profit if current profit is maximum.
- Update min_prices to always store the cheapest buying price.
- Ensures buy happens before sell.
Time Complexity: O(n)
Space Complexity: O(1)

"""
class Solution:
    def maxProfit(self,price:list[int])->int:
        min_prices=price[0]
        profit=0
        for i in range(1,len(price)):
            curr_profit = price[i]-min_prices
            if curr_profit>profit:
                profit = curr_profit
            min_prices=min(min_prices,price[i])
        return profit
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
            
            