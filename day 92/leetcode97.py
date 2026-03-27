class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        temp = []
        for i in range(0,n):
            if nums[i] != 0:
                temp.append(nums[i])
        nz = len(temp)
        for i in range(0,nz):
            nums[i] = temp[i]
        
        for i in range(nz,n):
            nums[i] = 0

        return nums
Solution = Solution()
print(Solution.moveZeroes([0,1,0,3,12]))
print(Solution.moveZeroes([0,0,5,9,9,7,3]))
