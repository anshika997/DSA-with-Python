class Solution:
    def frequencySort(self, s):

        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        result = ""

        for ch, count in sorted_chars:
            result += ch * count

        return result
print(Solution().frequencySort("tree"))
print(Solution().frequencySort("cccaaa"))