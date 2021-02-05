# input is positive integer
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l < r:
            mi = (l + r + 1) // 2
            if mi * mi > x:
                r = mi - 1
            else:
                l = mi
        return r

# input is a float number
def sqrt(x, e):
    if x < 0:
        raise Exception('Invalid input!')
    if x == 0:
        return 0.0
    if x < 1:
        return 1 / sqrt(1 / x, e)
    l, r = 0, x
    while r - l >= e:
        m = (r - l) / 2 + l
        if m * m < x:
            l = m
        else:
            r = m
    return l


print(sqrt(0, 0.00001))
