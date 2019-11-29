def coffeeMachine(A, lo, hi):
    res = []
    A.sort(reverse=True)

    def dfs(curr, idx, arr):
        nonlocal res
        if lo <= curr <= hi:
            res = list(arr)
            return True
        if curr > hi:
            return False
        for i in range(idx, len(A)):
            if dfs(curr + A[i], i, arr + [A[i]]):
                return True
        return False

    return dfs(0, 0, []), res


print(coffeeMachine([2, 5, 6], 10, 12))
