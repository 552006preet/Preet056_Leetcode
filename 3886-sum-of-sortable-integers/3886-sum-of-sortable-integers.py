
class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        def check(k):
            prev = float('-inf')

            for i in range(0, n, k):
                block = nums[i:i + k]
                smallest = min(block)
                largest = max(block)

                if smallest < prev:
                    return False

                drops = 0

                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        drops += 1

                if drops > 1:
                    return False

                prev = largest

            return True

        for k in range(1, n + 1):
            if n % k == 0 and check(k):
                ans += k

        return ans
