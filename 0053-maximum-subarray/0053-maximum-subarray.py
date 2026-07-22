class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx=-sys.maxsize-1
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            mx=max(sum,mx)
            if sum<0 :
                sum=0
        return mx

        