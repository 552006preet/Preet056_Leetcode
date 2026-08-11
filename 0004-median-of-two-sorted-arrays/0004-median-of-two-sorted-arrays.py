class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=len(nums1)
        m=len(nums2)

        n=nums1+nums2
        n.sort()
        left=0
        right=len(n)
        while left<=right:
            mid=left+(right-left)//2
            if (l+m)%2!=0:
                return n[mid]
            else:
                return (n[mid]+n[mid-1])/2
        