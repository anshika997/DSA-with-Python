class Solution:
    def singleNonDuplicate(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range (n):

            if i == 0:
                if nums[i] != nums[i+1] :
                    return nums[i]
            elif i == n-1 :
                if nums[i] != nums[i-1] :
                    return nums[i]
            else :
                if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                    return nums[i]
        return -1

print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(Solution().singleNonDuplicate([3,3,7,7,10,11,11]))