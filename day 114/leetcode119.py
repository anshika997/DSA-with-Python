class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine = list(magazine)
        if ransomNote == magazine :
            return True 
        for r in ransomNote: 
            found = False
            for m in range(len(magazine)): 
                if r == magazine[m] :
                    found  = True
                    magazine[m] = '#'
                    break
            if not found:
                return False
            
        return True     


Solution = Solution()
print(Solution.canConstruct("a", "b")) # False
print(Solution.canConstruct("aa", "ab")) # False    
print(Solution.canConstruct("aa", "aab")) # True
