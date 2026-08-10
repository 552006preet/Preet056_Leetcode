class Solution:
    def reverseWords(self, s: str) -> str:
        w=s.split()
        w.reverse()
        s=" ".join(w)
        return s