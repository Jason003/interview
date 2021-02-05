import math
def rotate_times(A, B):
    n = len(A)
    m = math.ceil(n ** 0.5)
    loc = {A[i] : i for i in range(m)}
    for i in range(0, n, m):
        if B[i] in loc:
            res = abs(loc[B[i]] - i)
            return min(res, n - res)
import random
for i in range(100):
    num = list({random.randint(0, 1000) for _ in range(100)})
    for j in range(len(num)):
        num2 = num[j:] + num[:j]
        assert min(j, len(num) - j) == rotate_times(num, num2)
