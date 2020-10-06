from functools import lru_cache


class Solution(object):
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)

        @lru_cache(None)
        def dp(id):
            if id == len(s):
                return [[]]
            ans = []
            cur = ""
            for i in range(id, len(s)):
                cur += s[i]
                if cur in wordDict:
                    for post_text in dp(i + 1):
                        ans.append([cur] + post_text)
            return ans

        ans = dp(0)
        return [" ".join(track) for track in ans]


main = Solution()
print(main.wordBreak("pineapplepenapple",
                     ["apple", "pen", "applepen", "pine", "pineapple"]))
