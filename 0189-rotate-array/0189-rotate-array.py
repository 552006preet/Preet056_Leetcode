class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums) #to avoid the unnecessary notations we use this like if k=9 and n=7 so to avoid doing 9 notation we apply modulo which in this case is 9%7=2 so we only do 2 notations rather than 2 
        nums.reverse()

        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])
        return nums
        
        
        

   
     
        
        
        
      
         
       
      
        

        