class solution:
    def maximumWealth(self,accounts:list[int])->int:
        ans = 0
        for account in accounts:
            ans = max(ans,sum(account))
        return ans
sol=solution()
print(sol.maximumWealth([[1,2,3],[3,2,1]]))