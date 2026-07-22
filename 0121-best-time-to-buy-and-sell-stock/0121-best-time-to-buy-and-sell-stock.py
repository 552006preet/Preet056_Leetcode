class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn=prices[0]
        profit=0
        for i in range(len(prices)):
            cost=prices[i]-mn
            profit=max(cost,profit)
            mn=min(mn,prices[i])
        return profit
        