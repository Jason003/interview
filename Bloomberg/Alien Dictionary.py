import collections
class Solution:
    def alienOrder(self, words) -> str:
        pre = collections.defaultdict(set)
        is_pre = collections.defaultdict(set)
        allChar = set(''.join(words))
        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]
            flag = False
            for c in range(min(len(a), len(b))):
                if a[c] != b[c]:
                    flag = True
                    pre[b[c]].add(a[c])
                    is_pre[a[c]].add(b[c])
                    break
            if not flag and len(a) > len(b): return ''
        res = []
        dq = collections.deque([c for c in allChar if not pre[c]])
        while dq:
            cur = dq.popleft()
            res.append(cur)
            for nxt in is_pre[cur]:
                pre[nxt].discard(cur)
                if not pre[nxt]:
                    dq.append(nxt)
        return ''.join(res) if len(res) == len(allChar) else ''