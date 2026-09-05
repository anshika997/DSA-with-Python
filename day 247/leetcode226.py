class Solution:
    def flipAndInvertImage(self, image) :

        result = []

        for i in range(len(image)):

            row = image[i][::-1]

            for j in range(len(row)):

                if row[j] == 1:
                    row[j] = 0
                else:
                    row[j] = 1

            result.append(row)

        return result
Solution = Solution()
print(Solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))