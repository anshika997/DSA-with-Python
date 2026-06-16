class Solution:
    def largestOddNumber(self, num):
        for i in range(len(num)-1,-1,-1):
            if (int(num[i]))%2==1:
                return num[:i+1]
        return ""
print(Solution().largestOddNumber("52"))
print(Solution().largestOddNumber("4206"))