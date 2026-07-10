class Solution:
    def singleNumber(self, nums):
        count = {}
        result = []

        # Count frequency
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        # Store all numbers with frequency 1
        for num in count:
            if count[num] == 1:
                result.append(num)

        return result
Solution = Solution()
print(Solution.singleNumber([1, 2, 1, 3, 2, 5]))
print(Solution.singleNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))