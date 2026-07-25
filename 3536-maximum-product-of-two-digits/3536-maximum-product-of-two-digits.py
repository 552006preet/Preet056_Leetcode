class Solution:
    def maxProduct(self, n: int) -> int:
        s=str(n)
        max1 = max2 = 0
        for i in s:           
            digit = int(i)
            if digit > max1:      
                max1, max2 = digit, max1
            elif digit > max2:    
                max2 = digit
        return max1 * max2    

        