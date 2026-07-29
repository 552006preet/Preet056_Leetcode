class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx=-sys.maxsize-1
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            mx=max(mx,total)
            if total<0:
                total=0
        return mx