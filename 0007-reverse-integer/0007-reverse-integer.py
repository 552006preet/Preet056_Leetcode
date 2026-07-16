class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        x *=sign
        rev=0
        temp=0
        while x>0:
            temp=x%10
            rev=rev*10+temp
            x//=10
            
        rev *=sign #set the given limit or range of int
        if rev< -2**31 or rev>2**31 -1:
            return 0
        return rev   