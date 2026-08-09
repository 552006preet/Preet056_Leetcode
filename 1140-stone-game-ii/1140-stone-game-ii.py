class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        s=[0]*(n+1)
        for i in range(n-1,-1,-1):
            s[i]=s[i+1]+piles[i]
        
        @lru_cache(None)
        def dp(i,m):
            if i >=n:
                return 0
            if 2*m>=n-i:
                return s[i]
            best=0
            for j in range(1,2*m+1):
                best=max(best,s[i]-dp(i+j,max(m,j)))
            return best
        return dp(0,1)