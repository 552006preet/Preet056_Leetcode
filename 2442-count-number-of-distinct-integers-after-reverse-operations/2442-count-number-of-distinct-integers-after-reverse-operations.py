class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new=[]
        for i in nums:
            new.append(int(str(i)[::-1]))
        nums+=new
        nums=set(nums)
        return len(nums)