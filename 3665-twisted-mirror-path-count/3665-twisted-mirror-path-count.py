class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        dp = [1] + [0] * (len(grid[0]) - 1)

        for row in grid:
            left = 0

            for j in range(len(row)):
                if row[j] == 1:
                    left, dp[j] = dp[j], left
                else:
                    left = (left + dp[j]) % MOD
                    dp[j] = left

        return left