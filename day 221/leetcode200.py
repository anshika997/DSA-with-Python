class Solution:
    def numJewelsInStones(self, jewels, stones) :
        count=0
        for stone in stones :
            if stone in jewels:
                count +=1
        return count
Solution = Solution()
print(Solution.numJewelsInStones("aA", "aAAbbbb"))
print(Solution.numJewelsInStones("z", "ZZ"))