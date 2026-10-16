class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        last = {}
        ans = 0
        total = 0

        def update(node, start, end, l, r):
            if l <= start and end <= r:
                old = tree[node]
                tree[node] += end - start + 1
                lazy[node] += 1
                return old

            mid = (start + end) // 2

            if lazy[node]:
                val = lazy[node]
                tree[node * 2] += val * (mid - start + 1)
                tree[node * 2 + 1] += val * (end - mid)
                lazy[node * 2] += val
                lazy[node * 2 + 1] += val
                lazy[node] = 0

            result = 0

            if l <= mid:
                result += update(node * 2, start, mid, l, r)

            if r > mid:
                result += update(node * 2 + 1, mid + 1, end, l, r)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]
            return result

        for i, num in enumerate(nums):
            l = last.get(num, -1) + 1

            old_sum = update(1, 0, n - 1, l, i)

            total = (total + 2 * old_sum + i - l + 1) % MOD
            ans = (ans + total) % MOD

            last[num] = i

        return ans