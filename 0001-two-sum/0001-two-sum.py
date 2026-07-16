class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     s={}
     com=0
     for i in range(len(nums)):
        com=target-nums[i]
        if com in s:
            return [s[com],i]
        s[nums[i]]=i




        