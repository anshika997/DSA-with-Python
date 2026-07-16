class Solution:
    def maximumProduct(self, nums):
        first = second = third = float('-inf')
        small1 = small2 = float('inf')

        for num in nums:

            # Find 3 largest numbers
            if num > first:
                third = second
                second = first
                first = num

            elif num > second:
                third = second
                second = num

            elif num > third:
                third = num

            # Find 2 smallest numbers
            if num < small1:
                small2 = small1
                small1 = num

            elif num < small2:
                small2 = num

        return max(first * second * third,
                   first * small1 * small2)
Solution = Solution()
print(Solution.maximumProduct([1,2,3,4,5]))
print(Solution.maximumProduct([6,7,8]))

