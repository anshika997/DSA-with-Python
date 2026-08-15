class Solution:
    def maxNumberOfBalloons(self, text) :
        result = 0
        freq = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
            }
        for i in text :
            if i in freq :
                freq[i]+=1
        while (freq['b'] >= 1 and

        freq['a'] >= 1 and
        freq['l'] >= 2 and
        freq['o'] >= 2 and
        freq['n'] >= 1):
            result +=1
            freq['n']-=1
            freq['b']-=1
            freq['a']-=1
            freq['l']-=2
            freq['o']-=2
    
        return result 
Solution = Solution()
print(Solution.maxNumberOfBalloons("nlaebolko"))
print(Solution.maxNumberOfBalloons("loonbalxballpoon"))