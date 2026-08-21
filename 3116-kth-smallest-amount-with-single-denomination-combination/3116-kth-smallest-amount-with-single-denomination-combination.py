class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        def count(x: int) -> int:
            total = 0
            m = len(coins)

            for mask in range(1, 1 << m):
                lcm = 1
                bits = 0
                for i in range(m):
                    if mask & (1 << i):
                        bits += 1
                        lcm = lcm * coins[i] // math.gcd(lcm, coins[i])
                        if lcm > x: 
                            break
                if lcm <= x:
                    if bits % 2 == 1:
                        total += x // lcm
                    else:
                        total -= x // lcm
            return total
        
        left, right = 1, max(coins) * k
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if count(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
