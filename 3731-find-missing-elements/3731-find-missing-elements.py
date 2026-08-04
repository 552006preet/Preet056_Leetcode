class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        sm,lg=min(nums),max(nums)
        l=[False]*(lg+1)
        for i in nums:
            l[i]=True
        ans=[]
        for i in range(sm,lg+1):
            if not l[i]:
                ans.append(i)
        return ans
        
        