from collections import defaultdict


class Solution(object):
    def shortestWay(self, source, target):
        ans = 1
        last = 0
        for char in target:
            last = source.find(char, last)
            if last == -1:
                last = source.find(char, 0)
                if last == -1:
                    return -1
                ans += 1
            last += 1
        return ans


main = Solution()
print(main.shortestWay("abc", "abcbc"))
