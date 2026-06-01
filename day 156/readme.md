📘 README – LeetCode 81: Search in Rotated Sorted Array II
Approach

I used a simple linear search approach.
I check whether the target exists in the array using the in operator.

Code
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        for i in range(n):
            if target in nums:
                return True
            else:
                return False
Dry Run

Input:

nums = [2,5,6,0,0,1,2]
target = 0

Check:

0 in nums

Output:

True

Input:

nums = [2,5,6,0,0,1,2]
target = 3

Check:

3 in nums

Output:

False
Complexity
Time Complexity: O(n)
Space Complexity: O(1)
Key Learning
target in nums checks whether the target exists in the list.
Returns True if found, otherwise False. 🚀