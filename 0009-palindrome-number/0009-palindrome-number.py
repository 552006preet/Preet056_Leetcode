class Solution:
    def isPalindrome(self, x: int) -> bool:
      revNum=0
      temp=0
      n=x
      
      while x>0:
        temp=x%10 
        revNum=(revNum*10)+temp
        x=x//10
      if n==revNum:
         return True
      elif n!=revNum:
        return False




 