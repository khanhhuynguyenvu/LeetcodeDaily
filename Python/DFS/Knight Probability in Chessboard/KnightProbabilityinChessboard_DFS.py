from functools import lru_cache


class Solution(object):
    def knightProbability(self, N, K, r, c):
        dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(K + 1)]

        @lru_cache(None)
        def dfs(k, x, y):
            if not (0 <= x < N and 0 <= y < N):
                return 0
            if k == 0:
                dp[k][x][y] = 1
                return 1
            for dr, dc in (-2, -1), (-2, 1), \
                          (-1, 2), (1, 2), \
                          (2, -1), (2, 1), \
                          (-1, -2), (1, -2):
                dp[k][x][y] += dfs(k - 1, x + dr, y + dc) / 8.0
            return dp[k][x][y]

        dfs(K, r, c)
        return dp[K][r][c]


main = Solution()
print(main.knightProbability(3, 3, 0, 0))