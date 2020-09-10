# # Stack O(N*M)
class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix) == 0:
            return 0
        n, m = len(matrix), len(matrix[0])
        dp = [0] * m

        def maxArea(hist):
            st = [-1]
            maxi = 0
            for i in range(m):
                while st[-1] != -1 and hist[st[-1]] >= hist[i]:
                    e = min(hist[st.pop()], i - st[-1] - 1)
                    maxi = max(maxi, e * e)
                st.append(i)
            while st[-1] != -1:
                e = min(hist[st.pop()], m - st[-1] - 1)
                maxi = max(maxi, e * e)
            return maxi

        ans = 0
        for i in range(n):
            for j in range(m):
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0
            ans = max(ans, maxArea(dp))
        return ans


main = Solution()
print(main.maximalRectangle(
    [["1", "0", "0", "1", "1", "0", "1", "1"],
     ["1", "0", "0", "0", "0", "1", "0", "0"],
     ["0", "1", "1", "1", "0", "0", "1", "1"],
     ["0", "0", "0", "1", "0", "0", "0", "1"],
     ["0", "0", "0", "0", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0", "1", "1", "0"],
     ["0", "1", "1", "0", "1", "1", "1", "0"]]
))
