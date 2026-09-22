class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        d=0
        # for i in range(len(nums)):
        #     d=target-nums[i]
        #     if d in s:
        #         return [s[d],i]
        #     s[nums[i]]=i 
        # or
        for i,num in enumerate(nums):
            d=target-num
            if d in s:
                return [s[d],i] 
            s[num]=i