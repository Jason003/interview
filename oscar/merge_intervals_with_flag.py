class Period:
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.val = val

    def __str__(self):
        return ' '.join(map(str, (self.start, self.end, self.val)))

def merge_intervals_with_flag(A, B):
    def merge_interval(a, b):
        s = max(a.start, b.start)
        e = min(a.end, b.end)
        if s < e:
            return Period(s, e, a.val and b.val)
    evens = sorted([(p.start, p.val) for p in A + B])
    res = []
    curr = True
    pre = None
print(merge_intervals_with_flag(None, None))