class Solution:
    def reverseOnlyLetters(self, s):
        l = 0
        r = len(s) - 1
        arr = list(s)

        while l < r:

            if not arr[l].isalpha():
                l += 1

            elif not arr[r].isalpha():
                r -= 1

            else:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        return "".join(arr)
Solution = Solution()
print(Solution.reverseOnlyLetters("ab-cd"))  # Output: "dc-ba"
print(Solution.reverseOnlyLetters("a-bC-dEf-ghIj"))  # Output: "j-Ih-gfE-dCba"
print(Solution.reverseOnlyLetters("Test1ng-Leet=code-Q!"))  # Output: "Qedo1ct-eeLg=ntse-T!"