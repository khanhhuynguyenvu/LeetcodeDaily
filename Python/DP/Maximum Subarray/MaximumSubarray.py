class Solution(object):
    def maxSubArray(self, nums):
        mini = 0
        total = 0
        ans = int(-1e12)
        for i in nums:
            total += i
            ans = max(ans, total - mini)
            mini = min(mini, total)
        return ans


main = Solution()
print(main.maxSubArray([2,-5,30]))
