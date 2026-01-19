# only valid for non-negative integers
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        mx = max(nums)
        freq=[0]*(mx+1)
        for i in nums:
            freq[i]+=1
        nums=[]
        for i in range(0,mx+1):
            while freq[i]>0:
                nums.append(i)
                freq[i]-=1
        return nums
sol=Solution()
print(sol.sortArray([5,2,3,1]))