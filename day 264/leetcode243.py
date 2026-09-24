class Solution:
    def summaryRanges(self, nums) :

        if not nums:
            return []

        start = 0
        i = 0
        result = []

        while i < len(nums) - 1:

            if nums[i] + 1 == nums[i + 1]:
                i += 1

            else:
                if start == i:
                    result.append(str(nums[i]))
                else:
                    result.append(str(nums[start]) + "->" + str(nums[i]))

                start = i + 1
                i += 1

        if start == i:
            result.append(str(nums[i]))
        else:
            result.append(str(nums[start]) + "->" + str(nums[i]))

        return result
Solution = Solution()
print(Solution.summaryRanges([0,1,2,4,5,7]))