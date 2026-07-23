class Solution:
    def halvesAreAlike(self, s): 
        vovels = "aeiouAEIOU"
        first_count = 0
        second_count = 0 
        mid = len(s)//2
        # first = s[:mid]
        # second = s[mid:]
        for ch in range(0,mid):
            if s[ch] in vovels:
                first_count+=1
            
        for ch in range(mid,len(s)):
            if s[ch] in vovels:
                second_count+=1
        return first_count==second_count
Solution = Solution()
print(Solution.halvesAreAlike("book"))  # Output: True
print(Solution.halvesAreAlike("textbook"))  # Output: False