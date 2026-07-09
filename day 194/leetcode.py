class Solution:
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            if num not in count :
                count[num] = 1
            else :
                count[num] += 1
            if count[num] > len(nums)//2:
                return num
Solution= Solution()
print(Solution.majorityElement([3,4,4,4]))
print(Solution.majorityElement([1,3,3]))
