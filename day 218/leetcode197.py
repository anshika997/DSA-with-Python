class Solution:
    def largestGoodInteger(self, num) :
        best = ""
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                current = num[i]*3
                if current>best:
                    best = current
        return best
Solution = Solution()
print(Solution.largestGoodInteger("6777133339"))
print(Solution.largestGoodInteger("2300019"))
print(Solution.largestGoodInteger("42352338"))