import collections


class Solution:
    def topKFrequent(self, words: List[str], k: int):
        cnt = collections.Counter(words)
        return sorted(list(cnt.keys()), key = lambda x : (-cnt[x], x))[:k]