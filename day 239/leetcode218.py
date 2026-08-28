class Solution:
    def xorOperation(self, n, start) :
        nums = []
        for i in range(n):
            nums.append(start+2*i)
        result = 0
        for j in range(len(nums)):
            result ^= nums[j]
        return result
Solution = Solution()
print(Solution.xorOperation(5,0))
print(Solution.xorOperation(4,3))