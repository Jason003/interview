'''
Count the number of prime numbers less than a non-negative number, n.
'''


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        flag = [True] * n
        flag[0] = flag[1] = False
        res = 0
        for i in range(2, n):
            if not flag[i]: continue
            res += 1
            j = 2
            while i * j < n:
                flag[i * j] = False
                j += 1
        return res


