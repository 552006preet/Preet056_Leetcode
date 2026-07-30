class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            x1=int(str(x)[::-1])
        else:
            x1=-int(str(-x)[::-1])
        
        if x1<-2**31 or x1>2**31-1:
            return 0

        return x1
        
        