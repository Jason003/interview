import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        # l, res = sorted(list(collections.Counter(s).items()), key = lambda x: -x[1]), ''
        # for k, v in l:
        #     res += k * v
        # return res

        cnt = collections.Counter(s)
        buckets = [[] for _ in range(max(cnt.values() or [0]) + 1)]
        for k, v in cnt.items():
            buckets[v].append(k)
        res = ''
        for i in range(len(buckets) - 1, 0, -1):
            for c in buckets[i]:
                res += i * c
        return res