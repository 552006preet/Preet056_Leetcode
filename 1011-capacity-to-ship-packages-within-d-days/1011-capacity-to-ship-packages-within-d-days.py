class Solution:
    def totaldays(self,weights:list[int],capacity:int):
        dayss=1
        crnt_load=0
        for w in weights:
            if crnt_load+w>capacity:
                dayss+=1
                crnt_load=w
            else:
                crnt_load+=w
        return dayss
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)

        while left<right:
            mid=left+(right-left)//2
            
            total=self.totaldays(weights,mid)

            if total<=days:
                right=mid
            else:
                left=mid+1
        return left