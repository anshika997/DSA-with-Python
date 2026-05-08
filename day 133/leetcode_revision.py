class Solution:
    def removeElement(self, nums,val):
        temp = []

        for num in nums:
            if num != val:
                temp.append(num)

        for i in range(len(temp)):
            nums[i] = temp[i]

        return len(temp)
Solution = Solution()
print(Solution.removeElement([3, 2, 2, 3], 3 ))
print(Solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2] , 2))