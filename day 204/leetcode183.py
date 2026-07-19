class Solution:
    def duplicateZeros(self, arr) :
        temp = []

        for num in arr:
            temp.append(num)

            if num == 0:
                temp.append(0)

        for i in range(len(arr)):
            arr[i] = temp[i]


# Driver Code (VS Code ke liye)
arr = list(map(int, input("Enter array: ").split()))

obj = Solution()
obj.duplicateZeros(arr)

print(arr)