import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = collections.Counter()
        begin = end = 0
        n = len(s)
        res = 0
        mark = 0
        while end < n:
            cnt[s[end]] += 1
            if cnt[s[end]] == 2: mark += 1
            while mark:
                if cnt[s[begin]] == 2: mark -= 1
                cnt[s[begin]] -= 1
                begin += 1
            res = max(res, end - begin + 1)
            end += 1
        return res