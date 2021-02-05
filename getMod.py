import random
def getMod(a, b): # return a % b
    while a:
        if a < b: return a
        c = b
        while c <= a:
            c <<= 1
        a -= c >> 1
    return 0

for _ in range(1000000):
    b = random.randint(1, 10000)
    a = random.randint(1, 10000000)
    try:
        assert getMod(a, b) == a % b
    except:
        print(a, b)