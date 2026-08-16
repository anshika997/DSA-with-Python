    
class Solution :
    def findNumbers(self, nums):
        result = 0 
        for i in range(len(nums)):
            if len(str(nums[i]))%2 == 0 :
                result +=1
        return result
Solution = Solution()
print(Solution.findNumbers([344,4353,224,114,433,354,32,22,1]))