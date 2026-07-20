class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #using XOR
      nums.sort()
      j=0
      for i in nums:
        j ^=i 
        
      return j
     
       
       
       


        
     
         

        