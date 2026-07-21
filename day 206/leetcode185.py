class Solution:
    def sumOfUnique(self, nums):
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        total = 0

        for key, value in freq.items():
            if value == 1:
                total += key

        return total
Solution = Solution()
print(Solution.sumOfUnique([1, 2, 3, 2]))  # Output: 4
print(Solution.sumOfUnique([1, 1, 1, 1, 1]))  # Output: 0