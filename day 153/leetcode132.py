class Solution:
    def permute(self, nums):

        result = []

        def backtrack(path):

            # Permutation complete
            if len(path) == len(nums):
                result.append(path[:])
                return

            for num in nums:

                # Skip already used number
                if num in path:
                    continue

                # Choose
                path.append(num)

                # Explore
                backtrack(path)

                # Backtrack
                path.pop()

        backtrack([])

        return result
print(Solution().permute([1, 2, 3]))
print(Solution().permute([0, 1]))