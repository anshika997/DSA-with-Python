class Solution:
    def findComplement(self, num):
        binary = bin(num)[2:]# remove 0b
        result = ""
        for i in binary :
            if i == '0' :
                result +='1'
            else :
                result += '0'

        return int(result,2) # result with base 2 because we want decimal 

Solution = Solution()
print(Solution.findComplement(5)) # 2
print(Solution.findComplement(1)) # 0   
