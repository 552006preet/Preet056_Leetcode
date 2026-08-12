class Solution:
    def count_partitions(self,nums:List[int],max_sum:int)->int:
        partitions=1
        current_sum=0
        for i in nums:
            if current_sum+i<=max_sum:
                current_sum+=i
            else:
                partitions+=1
                current_sum=i
        return partitions 
    def splitArray(self, nums: List[int], k: int) -> int:
        left,right=max(nums),sum(nums)
        
        while left<right:
            mid=left+(right-left)//2
            if self.count_partitions(nums,mid)<=k:
                right=mid
            else:
                left=mid+1
        return left
        
