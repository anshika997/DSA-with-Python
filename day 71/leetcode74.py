from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], arr: List[int]) -> List[int]:
        n = len(arr)
        ans = {}
        st = []

        for i in range(n-1, -1, -1):
            while len(st) > 0 and st[-1] <= arr[i]:
                st.pop()

            if len(st) == 0:
                ans[arr[i]] = -1
            else:
                ans[arr[i]] = st[-1]

            st.append(arr[i])

        return [ans[x] for x in nums1]


# ------- Main Code -------

nums1 = [4,1,2]
arr = [1,3,4,2]

obj = Solution()
result = obj.nextGreaterElement(nums1, arr)

print("Next Greater Elements:", result)