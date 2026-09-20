class Solution:

    def reverseDegree(self, s: str) -> int:
        m = 0
        for i, char in enumerate(s, start=1):
            rev_val = 26 - (ord(char) - 97)
            m += rev_val * i
        return m