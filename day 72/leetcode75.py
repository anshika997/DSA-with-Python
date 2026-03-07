from typing import List

class Solution:
    def nextGreaterElements(self, arr: List[int]) -> List[int]:

        # Step 1: Make the array circular
        arr = arr + arr

        # Step 2: Get length of new array
        n = len(arr)

        # Step 3: Create result array
        ans = [0] * n

        # Step 4: Create stack
        st = []

        # Step 5: Traverse from right to left
        for i in range(n - 1, -1, -1):

            # Step 6: Remove smaller elements from stack
            while len(st) > 0 and st[-1] <= arr[i]:
                st.pop()

            # Step 7: If stack empty
            if len(st) == 0:
                ans[i] = -1

            # Step 8: Otherwise top is next greater
            else:
                ans[i] = st[-1]

            # Step 9: Push current element
            st.append(arr[i])

        # Step 10: Return only first half
        return ans[:len(ans)//2]


# Example array
arr = [1, 2, 1]

# Create object
obj = Solution()

# Call function
result = obj.nextGreaterElements(arr)

# Print result
print("Next Greater Elements:", result)

