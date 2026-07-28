class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstPos(nums,target):
            n=len(nums)
            s=-1
            l,r=0,n-1
            while l<=r:
                mid=l+(r-l)//2
                if nums[mid]==target:
                    s=mid
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return s
        def LastPos(nums,target):
            n=len(nums)
            s=-1
            l,r=0,n-1
            while l<=r:
                mid=l+(r-l)//2
                if nums[mid]==target:
                    s=mid
                    l=mid+1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return s
        return [firstPos(nums,target),LastPos(nums,target)]    