def findFirstUniqueChar(s):
    mark = 0
    seen = 0
    for c in s:
        if mark & (1 << ord(c)) == 0 and seen & (1 << ord(c)) == 0:
            mark |= (1 << ord(c))
            seen |= (1 << ord(c))
        else:
            mark &= ~(1 << ord(c))
    # for c in s:
    #     if mark & (1 << ord(c)):
    #         return c
    nonunique = 0
    for i in range(ord('a'), ord('z') + 1):
        if mark & (1 << i) == 0 and seen & (1 << i): nonunique += 1
    return nonunique

import random, collections
for i in range(1000):
    list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    s = ''
    for _ in range(100):
        s += list[random.randint(0, 25)]
    cnt = collections.Counter(s)
    assert findFirstUniqueChar(s) == len([v for v in cnt.values() if v > 1])