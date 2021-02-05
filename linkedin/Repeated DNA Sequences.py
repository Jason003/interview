import functools, collections
class Solution:
    def findRepeatedDnaSequences(self, s: 'str') -> 'List[str]':
        if len(s) < 10:
            return []
        mapp = {'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3}
        res = []
        curr = functools.reduce(lambda x, y: 4 * x + y, [mapp[c] for c in s[:10]])
        seen = collections.Counter({curr : 1})
        for i in range(0, len(s) - 10):
            curr = (curr - (4 ** 9) * mapp[s[i]]) * 4 + mapp[s[i + 10]]
            seen[curr] += 1
            if seen[curr] == 2:
                res.append(s[i + 1 : i + 11])
        return res