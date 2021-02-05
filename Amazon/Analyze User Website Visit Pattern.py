'''
We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.
'''
import collections
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        cnt = collections.defaultdict(set)
        curr = None
        l = []

        def helper(l, u):
            if len(l) >= 3:
                def dfs(curr, idx):
                    if len(curr) == 3:
                        cnt[tuple(curr)].add(u)
                        return
                    for i in range(idx, len(l)):
                        dfs(curr + [l[i]], i + 1)
                dfs([], 0)

        for u, t, w in sorted(zip(username, timestamp, website)):
            if u != curr:
                if curr:
                    helper(l, curr)
                l = [w]
                curr = u
            else:
                l.append(w)
                helper(l, u)
        mx = max(list(map(len, cnt.values())) or [0])
        return min(k for k in cnt if len(cnt[k]) == mx)