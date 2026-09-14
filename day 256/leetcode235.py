class Solution:
    def validMountainArray(self, arr):
        i = 0 
        if len(arr)<3:
            return False 
        if max(arr) == arr[0] or max(arr) == arr[-1] :
            return False    
        while i < len(arr) - 1 and arr[i] < arr[i + 1]:
            i += 1

        if  i == 0 or i == len(arr)-1 :
            return False

        while i < len(arr) - 1 and arr[i] > arr[i + 1]:
            i += 1

        return i==len(arr)-1
Solution = Solution()
print(Solution.validMountainArray([0,3,2,1]))