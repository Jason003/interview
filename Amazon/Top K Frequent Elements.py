class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        A = list(cnt.keys())

        def quickSelect(l, r):
            p = l
            for i in range(l, r):
                if cnt[A[i]] >= cnt[A[r]]:
                    A[p], A[i] = A[i], A[p]
                    p += 1
            A[p], A[r] = A[r], A[p]
            if p == k - 1:
                return
            elif p > k - 1:
                quickSelect(l, p - 1)
            else:
                quickSelect(p + 1, r)

        quickSelect(0, len(A) - 1)
        return A[: k]


import collections
class TopKFrequentElements:
    def __init__(self):
        self.freq2number = collections.defaultdict(set)
        self.number2freq = collections.Counter()


    def add(self, val):
        self.number2freq[val] += 1
        self.freq2number[self.number2freq[val]].add(val)
        self.freq2number[self.number2freq[val] - 1].discard(val)

    def getTopK(self, K):
        res = []
        for f in sorted(list(self.freq2number.keys()), reverse=True):
            for num in self.freq2number[f]:
                res.append(num)
                if len(res) == K: return res
        return res

t = TopKFrequentElements()
t.add(1)
t.add(1)
t.add(2)
t.add(2)
t.add(2)
t.add(2)
t.add(3)
print(t.getTopK(3))
t.add(4)
t.add(4)
t.add(4)
t.add(4)
t.add(4)
t.add(4)
t.add(4)
t.add(4)
t.add(5)
t.add(6)
t.add(7)
t.add(8)
t.add(1)
print(t.getTopK(3))