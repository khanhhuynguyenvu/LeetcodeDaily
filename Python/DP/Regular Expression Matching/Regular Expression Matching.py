class Solution(object):
    def isMatch(self, text, pattern):
        n = len(text)
        m = len(pattern)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = True
        for i in range(n, -1, -1):
            for j in range(m - 1, -1, -1):
                first_match = i < n and pattern[j] in {text[i], "."}
                if j <= m - 2 and pattern[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]


main = Solution()
print(main.isMatch("mississippi", "mis*is*ip*."))
