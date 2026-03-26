class Solution:
    def find132pattern(self, nums):
        stack = []
        second = float('-inf')   # this is nums[k]

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second:
                return True

            while stack and nums[i] > stack[-1]:
                second = stack.pop()

            stack.append(nums[i])

        return False
# Example usage:
solution = Solution()
print(solution.find132pattern([1, 2, 3, 4]))  # Output: False
print(solution.find132pattern([3, 1, 4, 2]))  # Output: True
print(solution.find132pattern([-1, 3, 2, 0]))  # Output: True