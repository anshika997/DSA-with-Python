class Solution:
    def uniqueMorseRepresentations(self, words) :
        Morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = []

        for word in words :
            code = ''
            for i in word:
                index = ord(i)-ord('a')
                code += Morse [index]
            result.append(code)
        return len(set(result))
Solution = Solution()
print(Solution.uniqueMorseRepresentations(["gin","zen","gig","msg"]))



        
        

        