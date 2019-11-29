def intersection(A, B):
    # A, B might have duplicates, result should not contain duplicates
    res = []
    i, j = 0, 0
    m, n = len(A), len(B)
    while i < m and j < n:
        if A[i] == B[j]:
            if not res or res[-1] != A[i]:
                res.append(A[i])
            i += 1
            j += 1
        else:
            if A[i] < B[j]:
                i += 1
            else:
                j += 1
    return res


def intersectionKArrays(A):  # A: List[List[int]]
    if not A:
        return []
    res = A[0]
    for i in A[1:]:
        res = intersection(res, i)
    return res


def union(A, B):
    # A, B might have duplicates, result should not contain duplicates
    res = []
    i, j = 0, 0
    m, n = len(A), len(B)

    def add(x):
        if not res or res[-1] != x:
            res.append(x)

    while i < m or j < n:
        if i == m:
            add(B[j])
            j += 1
        elif j == n:
            add(A[i])
            i += 1
        elif A[i] < B[j]:
            add(A[i])
            i += 1
        else:
            add(B[j])
            j += 1
    return res


import heapq


def unionKArrays(A):  # A: List[List[int]]
    if not A:
        return []
    n = len(A)
    heap = [(A[i][0], i, 0) for i in range(n)]
    heapq.heapify(heap)
    res = []
    while heap:
        val, i, j = heapq.heappop(heap)
        if not res or res[-1] != val:
            res.append(val)
        if j + 1 < len(A[i]):
            heapq.heappush(heap, (A[i][j + 1], i, j + 1))
    return res


def intersection_iter(A, B):
    # A, B might have duplicates, result can contain duplicates

    def getNext(it):
        res = None
        try:
            res = next(it)
        except:
            pass
        return res

    res = []
    a, b = next(A), next(B)
    while a != None and b != None:
        if a == b:
            if not res or res[-1] != a:
                res.append(a)
            a, b = getNext(A), getNext(B)
        elif a < b:
            a = getNext(A)
        else:
            b = getNext(B)
    return res


import random

for i in range(1000):
    A = sorted([random.randint(0, 100) for _ in range(100)])
    B = sorted([random.randint(0, 100) for _ in range(10)])

    assert sorted(list(set(A) & set(B))) == intersection_iter(iter(A), iter(B)) == intersection(A,
                                                                                                B) == intersectionKArrays(
        [A, B])
    assert union(A, B) == sorted(list(set(A) | set(B))) == unionKArrays([A, B])
