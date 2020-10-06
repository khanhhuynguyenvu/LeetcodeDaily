from bisect import bisect_left, insort_left, bisect_right


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        if k == 0: return []
        ans = []
        w = sorted(nums[0:k])
        for i in range(k, len(nums) + 1):
            ans.append((w[k // 2] + w[(k - 1) // 2]) / 2.0)
            if i == len(nums): break
            index = bisect_left(w, nums[i - k])
            print(w, index, nums[i - k])
            w.pop(index)
            insort_left(w, nums[i])
        return ans


main = Solution()
print(main.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
