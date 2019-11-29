import collections
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        cnt = collections.Counter()
        for s, e in intervals:
            cnt[s] += 1
            cnt[e] -= 1
        res = 0
        curr = 0
        for time in sorted(list(cnt.keys())):
            curr += cnt[time]
            res = max(res, curr)
        return res