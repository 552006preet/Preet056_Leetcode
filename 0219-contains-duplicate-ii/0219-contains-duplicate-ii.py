class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num={}
        for i in range(0,len(nums)):
            if nums[i] in num and abs(i-num[nums[i]])<=k:
                return True
            num[nums[i]]=i
        return False        




