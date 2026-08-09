class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n=len(arr)
        left,right=0,n-1

        while left<=right:
            mid=left+(right-left)//2
            miss=arr[mid]-(mid+1)
            if miss<k:
                left=mid+1
            else:
                right=mid-1
        return k+right+1