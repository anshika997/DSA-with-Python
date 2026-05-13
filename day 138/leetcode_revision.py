class Solution:
    def removeElement(self, nums,val):
        new_nums = []

        for num in nums:
            if num != val:
                new_nums.insert(len(new_nums), num)

        nums[:len(new_nums)] = new_nums

        return len(new_nums)
Solution = Solution()
print(Solution.removeElement([3, 2, 2, 3], 3 ))
print(Solution.removeElement([0, 1, 2, 2, 3 , 0, 4, 2] , 2))