"""

Maximum Subarray (Kadane’s Algorithm) – LeetCode 53

LeetCode 53: Maximum Subarray (Kadane's Algorithm)
Logic:
- We maintain a running sum (curr_sum) of the current subarray.
- max_sum stores the maximum subarray sum found so far.
- Add each element to curr_sum.
- If curr_sum becomes negative, reset it to 0 because
  a negative sum will reduce the sum of any future subarray.
- Update max_sum whenever curr_sum is greater than it.
Time Complexity: O(n)
Space Complexity: O(1)

"""
class solution:
    def Maximum_Subarray(self, nums:list[int])->int:
        curr_num=0
        max_sum = nums[0]
        for i  in range(len(nums)):
            curr_num+=nums[i]
            if curr_num>max_sum:
                max_sum=curr_num
            if curr_num<0:
                curr_num=0
        return max_sum
sol=solution()
print(sol.Maximum_Subarray([-2,1,-3,4,-1,2,1,-5,4]))
            

