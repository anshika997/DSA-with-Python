class Solution:
    def removeElement(self, nums,val):
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]  # last element laao
                n -= 1                # size kam karo
            else:
                i += 1

        return n
Solution = Solution()
print(Solution.removeElement([3, 2, 2, 3], 3    ))
print(Solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))  