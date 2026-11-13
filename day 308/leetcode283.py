class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        n = len(people)
        l = 0 
        r = n-1
        answer = 0 
        people.sort()
        while l <= r :
            if  people[l] + people[r] <= limit:
                l+=1 
            r -= 1
            answer += 1   
        return answer

Solution = Solution()
print(Solution.numRescueBoats([3,2,2,1],3))