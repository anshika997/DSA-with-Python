class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        maxi = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1

                left += 1

            maxi = max(maxi, right - left + 1)

        return maxi
Solution=Solution()
print(Solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))