# this is a solution for leetcode 112 problem but it is not the best solution because it uses extra space for the frequency array. The best solution is to use the fact that the numbers are between 1 and n and use the index of the array to mark the visited numbers. Here is the code for the best solution:

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

