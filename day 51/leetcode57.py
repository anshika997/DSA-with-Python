class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = int("".join([str(i) for i in digits]))
        s +=1
        result = list(str(s))
        return [int(i) for i in result]
sol = Solution()
print((sol.plusOne([9,9,9])))
        