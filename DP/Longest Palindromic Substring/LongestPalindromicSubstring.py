class Solution(object):
    def longestPalindrome(self, s):
        l, r = 0, -1
        n = len(s)
        d = [0] * n
        d1 = [0] * n
        ansl, ansr = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d[l + r - i], r - i + 1)
            while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d[i] = k
            k -= 1
            if i + k > r:
                r = i + k
                l = i - k
                if ansr - ansl < r - l:
                    ansl = l
                    ansr = r
        l, r = 0, -1
        for i in range(n):
            k = 0 if i > r else min(d1[l + r - i + 1], r - i)
            while 0 <= i - k - 1 and i + k < n and s[i - k - 1] == s[i + k]:
                k += 1
            d1[i] = k
            k -= 1
            if i + k > r:
                r = i + k
                l = i - k - 1
                if ansr - ansl < r - l:
                    ansl = l
                    ansr = r
        return s[ansl:ansr + 1]


main = Solution()
print(main.longestPalindrome("ba"))
