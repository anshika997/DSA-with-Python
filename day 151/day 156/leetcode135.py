class Solution:
    def search(self, nums, target):
        n = len(nums)

        for i in range(n):
            if target in nums:
                return True
            else:
                return False
Solution().search([1, 2, 3, 4, 5], 3)
print(Solution().search([1, 2, 3, 4, 5], 3))
print(Solution().search([1, 2, 3, 4, 5], 6))