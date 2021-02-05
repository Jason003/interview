import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res, begin, end, count, c, n = 0, 0, 0, 0, collections.Counter(), len(s)
        while end < n:
            if c[s[end]] == 1:
                count += 1
            c[s[end]] += 1
            while count > 0:
                if c[s[begin]] == 2:
                    count -= 1
                c[s[begin]] -= 1
                begin += 1
            if count == 0:
                res = max(res, end - begin + 1)
            end += 1
        return res

