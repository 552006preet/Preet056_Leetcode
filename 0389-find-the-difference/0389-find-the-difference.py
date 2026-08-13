class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r=0
        for char in s+t:
            r^=ord(char)
        return chr(r)