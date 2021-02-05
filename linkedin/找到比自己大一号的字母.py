def findGreaterThan(A, x):
    if not A:
        return None
    lo, hi = 0, len(A) - 1
    while lo <= hi:
        mi = (hi + lo) // 2
        if A[mi] <= x:
            lo = mi + 1
        else:
            hi = mi - 1
    return A[lo] if lo < len(A) else A[0]

def another(A, x):
    if not A:
        return None
    for a in A:
        if a > x:
            return a
    return A[0]
import random
for _ in range(10000):
    A = sorted([random.randint(0, 100) for _ in range(100)])
    x = random.randint(0, 100)
    assert findGreaterThan(A, x) == another(A, x)
