class Solution:
    def finalPrices(self, prices):
        result = []
        for i in range(len(prices)):
            price = prices[i]
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    price=prices[i]-prices[j]
                    break
            result.append(price)
        return result
Solution=Solution()
print(Solution.finalPrices([8,4,6,2,3]))    
print(Solution.finalPrices([1,2,3,4,5]))    