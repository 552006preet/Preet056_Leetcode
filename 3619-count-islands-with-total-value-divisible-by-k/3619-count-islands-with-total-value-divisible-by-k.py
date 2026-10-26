class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                stack = [(i, j)]
                total = 0

                while stack:
                    r, c = stack.pop()

                    if not (0 <= r < m and 0 <= c < n):
                        continue
                    if grid[r][c] == 0:
                        continue

                    total += grid[r][c]
                    grid[r][c] = 0

                    for nr, nc in ((r + 1, c), (r - 1, c),
                                   (r, c + 1), (r, c - 1)):
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                            stack.append((nr, nc))

                if total % k == 0:
                    ans += 1

        return ans