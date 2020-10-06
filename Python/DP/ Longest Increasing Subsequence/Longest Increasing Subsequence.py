class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums: return 0
        n = len(nums)
        st = []
        ans = 0
        for i, num in enumerate(nums):
            l, r = -1, len(st)
            while l < r - 1:
                m = l + (r - l) // 2
                if num <= st[m]:
                    r = m
                else:
                    l = m
            if 0 <= r < len(st):
                st[r] = num
            if not st or num > st[-1]:
                st.append(num)
            print(st, r)
            ans = max(ans, len(st))
        return ans


main = Solution()
print(main.lengthOfLIS([4, 10, 4, 3, 8, 9]))
