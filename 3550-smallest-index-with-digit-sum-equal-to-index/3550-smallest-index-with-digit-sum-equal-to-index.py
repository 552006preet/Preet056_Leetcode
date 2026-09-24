class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            if num==0 and i==0:
                return 0

            sum=0
            while num>0:
                sum+=num%10
                num=num//10
            if sum==i:
                return i
        return -1