class Solution(object):
    def addBoldTag(self, s, dict):
        intervals = []
        for word in dict:
            idx = s.find(word)
            while idx != -1:
                intervals.append([idx, idx + len(word)])
                idx = s.find(word, idx + 1)
        intervals.sort(key=lambda x: x[0])
        st = [] if not intervals else [intervals[0]]
        for start, end in intervals[1:]:
            if start > st[-1][1]:
                st.append([start, end])
            else:
                st[-1][1] = max(end, st[-1][1])
        ans = ""
        new_end = 0
        for start, end in st:
            ans += s[new_end:start] + "<b>" + s[start:end] + "</b>"
            new_end = end
        ans += s[new_end:]
        return ans


main = Solution()
print(main.addBoldTag(s="d", dict=["d"]))
