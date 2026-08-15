class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        j=0
        for i in nums:
            j=j^i

        if all(i==0 for i in nums):
            return 0    
        if j==0 :
            return len(nums)-1
        else:
            return len(nums)