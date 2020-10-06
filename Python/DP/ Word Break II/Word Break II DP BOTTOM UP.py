from functools import lru_cache


class Solution(object):
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        n = len(s)
        dp = [[] for i in range(n + 1)]
        dp[n] = [[]]
        ans = []
        for i in range(n - 1, -1, -1):
            for j in range(n, -1, -1):
                word = s[i:j]
                if word in wordDict:
                    for post_text in dp[j]:
                        dp[i].append([word] + post_text)
        return [" ".join(track) for track in dp[0]]


main = Solution()
print(main.wordBreak("pineapplepenapple",
                     ["apple", "pen", "applepen", "pine", "pineapple"]))
