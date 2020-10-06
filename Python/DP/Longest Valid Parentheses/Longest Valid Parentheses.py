class Solution(object):
    def longestValidParentheses(self, s):
        l, r = 0, 0
        ans = 0
        n = len(s)
        for i in range(n):
            if s[i] == "(": l += 1
            if s[i] == ")": r += 1
            if l == r:
                ans = max(ans, r + l)
            elif r > l:
                l, r = 0, 0
        l, r = 0, 0
        for i in range(n - 1, -1, -1):
            if s[i] == "(": l += 1
            if s[i] == ")": r += 1
            if l == r:
                ans = max(ans, r + l)
            elif l > r:
                l, r = 0, 0
        return ans


main = Solution()
print(main.longestValidParentheses("(())"))
