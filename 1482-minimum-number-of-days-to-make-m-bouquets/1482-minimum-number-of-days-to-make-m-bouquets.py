class Solution:
    def boq_count(self,bloomDay: list[int],days:int,m:int,k:int)->bool:
        boquet=0
        count=0
        for bloom in bloomDay:
            if bloom<=days:
                count+=1
                if count==k:
                    boquet+=1
                    count=0
            else:
                count=0
        return boquet>=m
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k>n:
            return -1
        high=max(bloomDay)
        low=min(bloomDay)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if self.boq_count(bloomDay,mid,m,k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans