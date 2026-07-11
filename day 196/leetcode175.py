class Solution:
    def intersect(self, nums1,nums2):
        final = []
        for num1 in nums1:
            if num1 in nums2:
                final.append(num1)
                nums2.remove(num1)
        return final
Solution=   Solution()
print(Solution.intersect([1, 2, 2, 1],[2, 2]))
print(Solution.intersect([4, 9, 5],[9, 4, 9, 8, 4]))
    