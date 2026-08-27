class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        result=0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                result +=1
        return result
Solution = Solution()
print(Solution.busyStudent([1,2,3],[3,2,7],4))
print(Solution.busyStudent([4],[4],4))
