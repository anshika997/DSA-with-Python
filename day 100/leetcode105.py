class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Traverse from right to left
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:   # check if digit is odd
                return num[:i + 1]     # return substring
        
        return ""   # if no odd digit found
Solution = Solution()
print(Solution.largestOddNumber("52"))  # Output: "5"
print(Solution.largestOddNumber("4206"))  # Output: ""
print(Solution.largestOddNumber("35427"))  # Output: "35427"