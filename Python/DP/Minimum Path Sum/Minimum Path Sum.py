from functools import lru_cache


class Solution(object):
    def minPathSum(self, grid):
        if not grid: return 0
        n = len(grid)
        m = len(grid[0])

        # TopDown
        @lru_cache(None)
        def dfs(x, y):
            if x == n - 1 and y == m - 1: return grid[x][y]
            ans = 1e9
            for dr, dc in (0, 1), (1, 0):
                if 0 <= x + dr < n and 0 <= y + dc < m:
                    ans = min(ans, grid[x][y] + dfs(x + dr, y + dc))
            return ans

        # Bottom up
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                ans = 1e9
                for dr, dc in (0, 1), (1, 0):
                    if 0 <= i + dr < n and 0 <= j + dc < m:
                        ans = min(ans, grid[i + dr][j + dc])
                grid[i][j] += 0 if ans == 1e9 else ans
        return grid[0][0]


main = Solution()
print(main.minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))
