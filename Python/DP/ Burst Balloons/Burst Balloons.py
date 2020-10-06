from functools import lru_cache


class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)

        @lru_cache(None)
        def dp(l, r):
            if l == r - 1: return 0
            ans = 0
            for i in range(l + 1, r):
                ans = max(ans,
                          nums[l] * nums[i] * nums[r] + dp(l, i) + dp(i, r))
            return ans

        return dp(0, n - 1)


main = Solution()
print(main.maxCoins([3, 1]))
