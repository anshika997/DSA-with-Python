class Solution:
    def average(self, salary):
        
        return ((sum(salary))- (min(salary)) - (max(salary))) /(len(salary)-2)
Solution = Solution()
print(Solution.average([4000,3000,1000,2000]))
print(Solution.average([1000,2000,3000]))