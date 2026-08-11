class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        seen={}
        for i in nums1:
            seen[i]=True

        for j in nums2:
            if j in seen:
                return j
        return -1