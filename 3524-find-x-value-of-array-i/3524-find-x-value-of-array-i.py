class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        dp = [0] * k  # dp[r] = count of subarrays ending here with product % k == r
        
        for num in nums:
            next_dp = [0] * k
            val = num % k
            
            # Start a new subarray with just `num`
            next_dp[val] = 1
            
            # Extend existing subarrays ending at the previous position
            for r in range(k):
                if dp[r] > 0:
                    next_dp[(r * val) % k] += dp[r]
            
            # Accumulate the current counts into the answer array
            for r in range(k):
                ans[r] += next_dp[r]
                
            dp = next_dp
            
        return ans