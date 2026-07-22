class Solution:
    def relativeSortArray(self, arr1, arr2):
        result = []
        remaining = []
        for num in arr2:
            for x in arr1:
                if x == num:
                    result.append(x)
        for x in arr1:
            if x not in arr2:
                remaining.append(x)

        remaining.sort()

        return result + remaining
Solution = Solution()
print(Solution.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))  # Output: [2,2,2,1,4,3,3,9,6,7,19]
print(Solution.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))  # Output: [22,28,8,6,17,44]