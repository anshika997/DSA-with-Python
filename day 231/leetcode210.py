class NumArray:
    def __init__(self, nums):
        self.nums = nums 

    def sumRange(self, left, right):
        result = 0
        for i in range(left,right+1):
            result += self.nums[i]
        return result
            
nums = [-2, 0, 3, -5, 2, -1]

solution = NumArray(nums)

print(solution.sumRange(0, 2))
print(solution.sumRange(2, 5))
print(solution.sumRange(0, 5))