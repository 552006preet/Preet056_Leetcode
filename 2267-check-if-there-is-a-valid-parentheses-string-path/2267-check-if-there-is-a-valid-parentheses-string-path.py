class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Quick checks
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        # Valid parentheses string must have even length
        if (m + n - 1) % 2:
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                balances = set()

                if i > 0:
                    balances |= dp[i - 1][j]

                if j > 0:
                    balances |= dp[i][j - 1]

                for balance in balances:
                    if grid[i][j] == '(':
                        dp[i][j].add(balance + 1)
                    elif balance > 0:
                        dp[i][j].add(balance - 1)

        return 0 in dp[m - 1][n - 1]