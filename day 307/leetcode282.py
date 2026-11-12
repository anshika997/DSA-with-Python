class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        result = []
        for i in nums :
            digits = []
            while i > 0 :
                digit = i%10
                digits.append(digit)
                i = i//10
            result.extend(digits[::-1])
        return  result 
Solution = Solution()
print(Solution.separateDigits([7,1,3,9]))
print(Solution.separateDigits([13,25,83,77]))