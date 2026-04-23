# but the question is to add two numbers represented as strings without converting them to integers directly. this is not the correct solution for the problem. we need to implement the addition manually by iterating through the digits of the strings and handling carry properly.
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = int(num1)
        num2 = int(num2)
        add = num1+num2
        return str(add)
Solution = Solution()
print(Solution.addStrings("11", "123"))
print(Solution.addStrings("456", "77"))