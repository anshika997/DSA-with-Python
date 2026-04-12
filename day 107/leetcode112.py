class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        freq = [0]*(n+1)
        for num in nums :
            freq[num] += 1
            if freq[num]>1:
                return num
Solution= Solution()
print(Solution.findDuplicate([1,3,4,2,2]))
print(Solution.findDuplicate([3,1,3,4,2]))
