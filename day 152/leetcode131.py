class Solution:
    def combinationSum(self, candidates, target):

        result = []

        def backtrack(index, path, total):

            # Target achieved
            if total == target:
                result.append(path[:])
                return

            # Out of bounds or exceeded target
            if index >= len(candidates) or total > target:
                return

            # Include current number
            path.append(candidates[index])

            backtrack(index, path, total + candidates[index])

            # Backtrack
            path.pop()

            # Skip current number
            backtrack(index + 1, path, total)

        backtrack(0, [], 0)

        return result
print(Solution().combinationSum([2, 3, 6, 7], 7))
print(Solution().combinationSum([2, 3, 5], 8))