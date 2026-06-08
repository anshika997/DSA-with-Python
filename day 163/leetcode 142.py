
class Solution:
    def singleNonDuplicate(self, arr):
        n = len(arr)
        if n == 1:
            return arr[0]
        if arr[0] != arr[1]:
            return arr[0]
        if arr[n - 1] != arr[n - 2]:
            return arr[n - 1]
        low, high = 1, n - 2
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
                return arr[mid]
            if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or \
               (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
                low = mid + 1
            else:
                high = mid - 1
        return -1
print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(Solution().singleNonDuplicate([3,3,7,7,10,11,11]))