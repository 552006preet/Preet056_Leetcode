class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        limit = left
        remaining = k - sum(max(0, d - limit) for d in diff)

        ans = 0

        for d in diff:
            d = min(d, limit)

            if d == limit and remaining > 0:
                d -= 1
                remaining -= 1

            ans += d * d

        return ans