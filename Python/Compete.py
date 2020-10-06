# class Solution(object):
#     def countSmaller(self, nums):
#         if not nums: return []
#         n = len(nums)
#         q = []
#         for i in range(n)[::-1]:
#             l, r = 0, len(q)
#             while l < r:
#                 m = (l + r) // 2
#                 if nums[i] <= q[m]:
#                     r = m
#                 else:
#                     l = m + 1
#             q[l:l] = [nums[i]]
#             nums[i] = l
#         return nums
#
#
# main = Solution()
# print(main.countSmaller([9, 7]))
a = [1, 2, 3]
a[2:2] = [4]
print(a)
