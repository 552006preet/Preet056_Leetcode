class Solution:
    def hours(self,piles:list[int],speed:int)->int:
        ttlhrs=0

        for bananas in piles:
            ttlhrs+=(bananas+speed-1)//speed
        return ttlhrs

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=max(piles)
        ans=n
        low,high=1,n

        while low<=high:
            mid=low+(high-low)//2

            hrs=self.hours(piles,mid)
            
            if hrs<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans