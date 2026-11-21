class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                 freq[i] +=1
        for i in freq :
            if freq[i]==1:
                return i 
Solution = Solution()
print(Solution.singleNumber([2,2,1]))