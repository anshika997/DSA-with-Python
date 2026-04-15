class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        binary = binary.zfill(32)
        binary_reverse = binary[::-1]
        return int(binary_reverse,2) 
Solution = Solution()
print(Solution.reverseBits(43261596))  # Output: 964176192  
print(Solution.reverseBits(4294967293))  # Output: 3221225471
