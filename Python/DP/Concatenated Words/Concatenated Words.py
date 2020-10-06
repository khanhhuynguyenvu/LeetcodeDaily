class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        words = set(words)
        min_len = min([len(i) for i in words])
        min_len = max(min_len, 1)

        def dp(s, num):
            if s in words and num > 0: return True
            for i in range(min_len, len(s) - min_len + 1):
                if s[:i] in words and dp(s[i:], num + 1):
                    return True
            return False

        ans = []
        for w in words:
            if len(w) >= 2 * min_len and dp(w, 0): ans.append(w)
        return ans


main = Solution()
print(main.findAllConcatenatedWordsInADict(
    ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]))
