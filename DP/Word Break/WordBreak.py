from collections import  deque


class Solution(object):
    def wordBreak(self, s, wordDict):
        if len(wordDict) == 0:
            return False
        q = deque()
        q.append(0)
        used = {}
        words = {}
        for word in wordDict:
            words[word] = 1
        maxi = max(len(w) for w in wordDict)
        d = [{} for i in range(len(s))]
        for i in range(len(s)):
            k = 0
            cur = ""
            while 0 <= i - k and k < maxi:
                cur = s[i - k] + cur
                if cur in words:
                    d[i][i - k] = 1
                k += 1
        while q:
            start = q.popleft()
            if start not in used:
                for end in range(start + 1, len(s) + 1):
                    if start in d[end - 1]:
                        q.append(end)
                        if end == len(s):
                            return True
                used[start] = 1
        return False


main = Solution()
print(main.wordBreak(s="a", wordDict=["ab"]))
