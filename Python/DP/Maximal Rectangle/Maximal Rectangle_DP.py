# DP O(N^2*M)
class Solution(object):
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        n, m = len(matrix), len(matrix[0])
        row = [[0] * m for i in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    row[i][j] = row[i][j - 1] + 1 if j > 0 else 1
                    width = row[i][j]
                    for up in range(i+1):
                        width = min(width, row[i-up][j])
                        ans = max(ans, (up + 1) * width)
        return ans


main = Solution()
print(main.maximalRectangle([
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]))
# print(main.maximalRectangle([["1"]]))
