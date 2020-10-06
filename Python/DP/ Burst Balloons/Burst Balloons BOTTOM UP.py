from functools import lru_cache


class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for left in range(n - 2, -1, -1):
            for right in range(left + 2, n):
                for i in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n-1]


main = Solution()
print(main.maxCoins([3, 1, 5, 8]))
