
class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        row = len(grid)
        column = len(grid[0])

        matrix = []

        for i in range(row - 2):
            result_row = []

            for j in range(column - 2):
                result = []

                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        result.append(grid[x][y])

                result_row.append(max(result))

            matrix.append(result_row)

        return matrix


# Test Case
grid = [
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2]
]

obj = Solution()

answer = obj.largestLocal(grid)

print("Original Matrix:")
for r in grid:
    print(r)

print("\nLargest Local Values:")
for r in answer:
    print(r)
