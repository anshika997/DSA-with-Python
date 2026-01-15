class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2)).replace("0b","")
sol=Solution()
print(sol.addBinary("11","1"))