class Solution:
    def sumOddLengthSubarrays(self, arr):
        result = 0 
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if (j-i+1) % 2 != 0:
                    for k in range(i, j+1):
                        result += arr[k]
        return result
Solution = Solution()
print(Solution.sumOddLengthSubarrays([1,4,2,5,3]))
print(Solution.sumOddLengthSubarrays([10,11,12]))