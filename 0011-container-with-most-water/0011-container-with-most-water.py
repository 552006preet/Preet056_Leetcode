class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n=len(height)
        left,right=0,n-1
        area=0
        
        while left<right:
            current_area=(right-left)*min(height[left],height[right])
            
            area=max(current_area,area)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return area