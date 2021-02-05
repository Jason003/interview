import collections
class FreqStack:

    def __init__(self):
        self.cnt = collections.Counter()
        self.mx = 0
        self.freqList = collections.defaultdict(list)

    def push(self, x: int) -> None:
        self.cnt[x] += 1
        self.mx = max(self.mx, self.cnt[x])
        self.freqList[self.cnt[x]].append(x)

    def pop(self) -> int:
        res = self.freqList[self.mx].pop()
        self.cnt[res] -= 1
        if not self.freqList[self.mx]:
            self.mx -= 1
        return res