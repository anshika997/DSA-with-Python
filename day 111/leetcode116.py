class Solution:
    def containsDuplicate(self, nums):
        n = len(nums)
        freq = {}
        for num in nums :
            freq[num] = freq.get(num, 0) + 1
            if freq[num]>1:
                return True
        return False
Solution = Solution()
print(Solution.containsDuplicate([1,2,3,1])) # True
print(Solution.containsDuplicate([1,2,3,4])) # False