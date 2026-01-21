class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m-1 
        j = n-1
        k = m+n-1
        while j>=0:
            if i < 0 or nums2[j]>nums1[i]:
                nums1[k]=nums2[j]
                k-=1
                j-=1
            else:
                nums1[k]=nums1[i]
                k-=1
                i-=1
sol = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sol.merge(nums1,m,nums2,n)
print(nums1)