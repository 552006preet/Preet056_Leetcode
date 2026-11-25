
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        mod1, mod2 = 10**9 + 7, 10**9 + 9
        base1, base2 = 100019, 100043

        def check(length):
            power1 = pow(base1, length, mod1)
            power2 = pow(base2, length, mod2)

            h1 = h2 = 0
            count = {}

            for i in range(n):
                h1 = (h1 * base1 + nums[i]) % mod1
                h2 = (h2 * base2 + nums[i]) % mod2

                if i >= length:
                    h1 = (h1 - nums[i - length] * power1) % mod1
                    h2 = (h2 - nums[i - length] * power2) % mod2

                if i >= length - 1:
                    key = (h1, h2)
                    count[key] = count.get(key, 0) + 1

            return any(v == 1 for v in count.values())

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
