class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * n for _ in range(n)]

        # Calculate minimum changes for every substring
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = length

                for d in range(1, length):
                    if length % d == 0:
                        changes = 0

                        for offset in range(d):
                            l = i + offset
                            r = j - d + 1 + offset

                            while l < r:
                                if s[l] != s[r]:
                                    changes += 1
                                l += d
                                r -= d

                        best = min(best, changes)

                cost[i][j] = best

        # DP: minimum changes to divide first i characters into j parts
        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for parts in range(1, k + 1):
                for start in range(i - 1):
                    if dp[start][parts - 1] != INF:
                        dp[i][parts] = min(
                            dp[i][parts],
                            dp[start][parts - 1] + cost[start][i - 1]
                        )

        return dp[n][k]