class solution:
    def uniquestring(self,s):
        freq={}
        ans=0
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i] +=1
        for i in range (len(s)):
            if freq[s[i]]==1:
                return i
        return -1
sol=solution()
print(sol.uniquestring("leetcode"))