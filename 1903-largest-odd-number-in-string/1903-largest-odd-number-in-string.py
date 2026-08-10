class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2==1:
                return num[:i+1] # work as sting[:6] as 0 to 6
        return ""