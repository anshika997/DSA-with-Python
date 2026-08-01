class Solution:
    def interpret(self, command):
        word = command
        word = word.replace('()','o')
        word = word.replace('(al)','al')
        return word
Solution = Solution()
print(Solution.interpret("G()(al)"))
print(Solution.interpret("G()()()()(al)"))
