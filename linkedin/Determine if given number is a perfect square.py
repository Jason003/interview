def is_square(n):
    if n < 0:
        return False

    lo, hi = 0, n
    while lo <= hi:
        mi = (hi - lo) // 2 + lo
        temp = mi * mi
        if temp == n:
            return True
        elif temp < n:
            lo = mi + 1
        else:
            hi = mi - 1
    return False


for i in range(1000000):
    assert is_square(i) == (int((int(i ** 0.5)) ** 2) == i)
