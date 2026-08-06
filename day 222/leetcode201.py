class Solution:
    def checkString(self, s):
        check_b = False

        for ch in s:

            if ch == 'b':
                check_b = True

            elif ch == 'a' and check_b:
                return False

        return True
Solution = Solution()
print(Solution.checkString("aaabbb"))
print(Solution.checkString("abab"))
print(Solution.checkString("bbb"))