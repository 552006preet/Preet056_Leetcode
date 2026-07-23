class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l=[ch.lower() for ch in s if ch.isalnum()]
        if l==l[::-1]:
            return True
        return False
        

     
     
                
                
   
    
            
            

            
                

            
            
        