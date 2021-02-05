def combination(a, b):
    def fac(x):
        res = 1
        for i in range(2, x + 1):
            res *= i
        return res
    return fac(a) // (fac(b) * fac(a - b))

print(combination(10, 1))