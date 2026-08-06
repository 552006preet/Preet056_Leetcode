class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        j=0
        for i in nums:
            j= j^i
        return j        
            