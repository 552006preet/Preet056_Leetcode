class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        d=s.split()
        lnth=len(d[-1])
        return lnth