class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i=len(s)
        j=len(t)

        if i!=j:
            return False

        countS=Counter(s)
        countT=Counter(t)
        if countS==countT:
            return True
        return False