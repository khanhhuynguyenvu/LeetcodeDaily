class Solution(object):
    def numDecodings(self, s):
        d = [1, 1, 0]
        for i in range(len(s)):
            d[2] = 0
            if 0 < ord(s[i]) - ord('0') < 10:
                d[2] += d[1]
            if 0 < i and 9 < (ord(s[i]) - ord('0')) + (ord(s[i - 1]) - ord('0')) * 10 < 27:
                d[2] += d[0]
            d[0] = d[1]
            d[1] = d[2]
        return d[2]


main = Solution()
print(main.numDecodings("10231"))
