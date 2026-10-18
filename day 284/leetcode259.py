class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = {}
        for i in range(len(arr)):
            if arr[i] not in freq :
                freq[arr[i]] = 1
            else:
                freq[arr[i]] += 1
        return len(freq.values()) == len(set(freq.values())) 
Solution = Solution()
print(Solution.uniqueOccurrences([1,2,2,1,1,3]))