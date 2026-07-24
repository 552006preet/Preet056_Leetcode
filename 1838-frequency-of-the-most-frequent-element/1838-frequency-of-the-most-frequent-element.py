class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        j=0
        t=0
        r=1
        for i in range(len(nums)):
            t+=nums[i]
            while nums[i]*(i-j+1)-t>k:
                t-=nums[j]
                j+=1
            r=max(r,i-j+1)
        return r

        