import collections
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def generate(s):
            mapp = collections.defaultdict(list)
            for i, c in enumerate(s):
                mapp[c].append(i)
            return list(mapp.values())
        return generate(s) == generate(t)


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cnt1, cnt2 = collections.defaultdict(lambda: 0), collections.defaultdict(lambda: 0)
        for i in range(len(s)):
            if cnt1[s[i]] != cnt2[t[i]]: return False
            cnt1[s[i]] = i + 1
            cnt2[t[i]] = i + 1
        return True