class Solution:
    def isPalindrome(self, s: str) -> bool:
        sh=[ch.lower() for ch in s if ch.isalnum()]
        if sh==sh[::-1]:
            return True
        return False