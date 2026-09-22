class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n=len(height)
        left,right=0,n-1
        area=0
        
        while left<right:
            area=max(area,(right-left)*min(height[left],height[right]))

            if height[left]<height[right]:
                left+=1
            elif height[right]<height[left]:
                right-=1
            else:
                left+=1
        return area