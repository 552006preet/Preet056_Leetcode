class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[]
        
        for i in nums:
            s=i*i
            l.append(s)
        l.sort()
        return l
