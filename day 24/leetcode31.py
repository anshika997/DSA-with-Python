class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) ->list[int]:
        set1=set(nums1)
        set2=set(nums2)
        return list(set1.intersection(set2))
sol = Solution()
print(sol.intersection([1,2,2,1],[2,2]))