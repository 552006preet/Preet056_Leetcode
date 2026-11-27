
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for factor, price in items)

        # Count free items obtained from buying each type once
        free = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        # 0/1 Knapsack: first purchase of each item type
        dp = [-1] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            factor, price = items[i]

            for b in range(budget, price - 1, -1):
                if dp[b - price] != -1:
                    dp[b] = max(
                        dp[b],
                        dp[b - price] + 1 + free[i]
                    )

        # Spend remaining budget on cheapest items
        ans = 0

        for spent in range(budget + 1):
            if dp[spent] != -1:
                extra = (budget - spent) // min_price
                ans = max(ans, dp[spent] + extra)

        return ans
