def numTrees(n):
    """
    :type n: int
    :rtype: int
    """
    d = {}
    def helper(lo, hi):
        if hi <= lo: return 1
        if (lo, hi) in d: return d[(lo, hi)]
        res = 0
        for i in range(lo, hi + 1):
            res += helper(lo, i - 1) * helper(i + 1, hi)
        d[(lo, hi)] = res
        return res

    return helper(1, n)



def winning_possibility(possibility):
    mem = {}
    def helper(idx, cnt):
        if idx == len(possibility):
            if cnt >= 4: return 1
            return 0
        if (idx, cnt) in mem: return mem[idx, cnt]
        mem[idx, cnt] = possibility[idx] * helper(idx + 1, cnt + 1) + (1 - possibility[idx]) * helper(idx + 1, cnt)
        return mem[idx, cnt]
    return helper(0, 0)

print(winning_possibility([0.1,0.5,0.5,1,1,1,0]))
print(winning_possibility([1,1,1,1,1,1,0]))
