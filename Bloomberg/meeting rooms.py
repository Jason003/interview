import collections
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        cnt = collections.Counter()
        for i, j in intervals:
            cnt[i] += 1
            cnt[j] -= 1
        res = 0
        curr = 0
        for t in sorted(list(cnt.keys())):
            curr += cnt[t]
            res = max(curr, res)
        return res
