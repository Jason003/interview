'''
第二题，问一个数组里面 只有0, 1，2。 问i<j<k 并且 ai<aj<ak的有多少。想了个比较复杂的解法。面试官提示，专注0,1对，先不看2。然后我给了个DP解法，O（n）。
'''

def sol1(A):
    res = 0
    n = len(A)
    for i in range(n):
        if A[i] == 0:
            for j in range(i + 1, n):
                if A[j] == 1:
                    for k in range(j + 1, n):
                        res += int(A[k] == 2)
    return res

def sol2(A):
    res = 0
    n = len(A)
    cnt0 = [0] * n
    cnt2 = [0] * n
    for i in range(n):
        cnt0[i] = (cnt0[i - 1] if i > 0 else 0) + int(A[i] == 0)
    for i in range(n - 1, -1, -1):
        cnt2[i] = (cnt2[i + 1] if i < n - 1 else 0) + int(A[i] == 2)
    for i in range(n):
        res += (A[i] == 1) * cnt0[i] * cnt2[i]
    return res

import random
# for _ in range(100):
#     A = [random.randint(0, 2) for _ in range(100)]
#     assert sol1(A) == sol2(A)
A = [random.randint(0, 2) for _ in range(10000)]
print(sol2(A))
print(sol1(A))