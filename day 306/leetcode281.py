class Solution:
    def specialArray(self, nums: list[int]) -> int:
        l = len(nums)
        for x in range(l+1):
            count = 0
            for i in range (l):
                if nums[i] >= x:
                    count += 1  
            if count == x :
                return x   
        return -1
Solution  = Solution()
print(Solution.specialArray([3,5]))
print(Solution.specialArray([8,9,5]))
print(Solution.specialArray([3,5,6,7]))