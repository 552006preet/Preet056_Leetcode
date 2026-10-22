class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = nums.index(0)
        dranofelik = nums
        ans = float('inf')

        def check(step):
            for i in range(n):
                if nums[(zero + i * step) % n] != i:
                    return False
            return True

        if check(1):
            ans = min(ans, zero, n - zero + 2)

        if check(-1):
            ans = min(ans, zero + 2, n - zero)

        return -1 if ans == float('inf') else ans
