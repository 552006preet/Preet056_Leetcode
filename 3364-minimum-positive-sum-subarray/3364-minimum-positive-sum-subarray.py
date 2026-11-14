class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')
        n = len(nums)

        for size in range(l, r + 1):
            curr = sum(nums[:size])

            if curr > 0:
                ans = min(ans, curr)

            for i in range(size, n):
                curr += nums[i] - nums[i - size]

                if curr > 0:
                    ans = min(ans, curr)

        return -1 if ans == float('inf') else ans