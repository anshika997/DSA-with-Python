"""
PROBLEM : Sort Array by Parity leetcode 905

Logic Explanation:

- 'start' keeps track of where the next even number should be placed.
- When an even number is found at index i:
- we swap nums[i] with nums[start].
- This ensures all even numbers are moved to the front.
- Swapping is safe even when i == start and keeps the code simple.
- Time Complexity: O(n)
- Space Complexity: O(1)
"""

class Solution:
    def Sort_Array_by_Parity(self,nums:list[int])->list[int]:
        n = len(nums)
        start = 0
        for i in range(n):
            if nums[i]%2==0:
                # here we swap 
                temp = nums[i]
                nums[i]= nums[start]
                nums[start]=temp
                start+=1
        return nums
sol = Solution()
print(sol.Sort_Array_by_Parity([3,1,2,4]
))        
