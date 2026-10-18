
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        arr = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
        pos = {num: i for i, num in enumerate(arr)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            j = i
            count = 0

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                count += 1

            swaps += count - 1

        return swaps
