class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        seen={}
        result=[]
        for i in nums:
            seen[i]=seen.get(i,0)+1
        result=sorted(seen,key=seen.get,reverse=True)
        return result[:k]
        