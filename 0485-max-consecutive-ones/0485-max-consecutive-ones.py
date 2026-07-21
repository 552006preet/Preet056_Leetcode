class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx=0
        ct=0
        for i in range(len(nums)):
            if nums[i]==1:
                ct+=1
                mx=max(mx,ct)
            else:
                ct=0
        return mx
        