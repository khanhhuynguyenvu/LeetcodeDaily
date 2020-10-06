class Solution(object):
    def maxProfit(self, prices):
        mini = int(1e9)
        ans = 0
        for price in prices:
            ans = max(ans, price - mini)
            mini = min(mini, price)
        return ans


main = Solution()
print(main.maxProfit([5, 4, 3]))
