class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        while True :
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast :
                break 

        slow = nums[0]
      
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow 
Solution= Solution()
print(Solution.findDuplicate([1,3,4,2,2]))  
print(Solution.findDuplicate([3,1,3,4,2]))
