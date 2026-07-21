class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)-1
        low,high=0,n
        
       
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1   
        return low    
            
             
             
               
            
               
             
          
             
             

        