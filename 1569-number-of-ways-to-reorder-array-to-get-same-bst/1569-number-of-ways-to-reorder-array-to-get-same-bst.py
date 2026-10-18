
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        from math import comb

        MOD = 10**9 + 7

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            ways = comb(len(left) + len(right), len(left))

            return ways * dfs(left) * dfs(right) % MOD

        return (dfs(nums) - 1) % MOD
