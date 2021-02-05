import random
def addStrings(num1: str, num2: str) -> str:
    d1 = list(map(int, list(str(num1))[::-1]))
    d2 = list(map(int, list(str(num2))[::-1]))
    res = []
    i, j = 0, 0
    rem = 0
    while i < len(d1) or j < len(d2) or rem:
        rem += (d1[i] if i < len(d1) else 0) + (d2[j] if j < len(d2) else 0)
        i += 1
        j += 1
        res.append(rem % 10)
        rem //= 10
    return ''.join(map(str, res))[::-1]

def minus(num1, num2): # num1 > num2
    d1 = list(map(int, list(str(num1))[::-1]))
    d2 = list(map(int, list(str(num2))[::-1]))
    res = []
    i, j = 0, 0
    rem = 0
    while i < len(d1) or j < len(d2) or rem:
        temp = d1[i] - (d2[j] if j < len(d2) else 0) + rem
        if temp < 0:
            res.append(temp + 10)
            rem = -1
        else:
            res.append(temp)
            rem = 0
        i += 1
        j += 1
    return ''.join(map(str, res))[::-1].lstrip('0') or '0'





def addString2(num1, num2):
    if not num1 or not num2: return num1 if not num2 else num2
    def negative(num):
        return num[0] == '-'
    if not negative(num1) and not negative(num2): return addStrings(num1, num2)
    elif negative(num1) and negative(num2): return '-' + addStrings(num1[1:], num2[1:])
    else:
        if negative(num1) and not negative(num2):
            pos_num, neg_num = num2, num1
        else:
            pos_num, neg_num = num1, num2
        neg = len(pos_num) < len(neg_num[1:]) or (pos_num < neg_num[1:] and len(pos_num) == len(neg_num[1:]))
        if neg: return '-' + minus(neg_num[1:], pos_num)
        else: return minus(pos_num, neg_num[1:])



for _ in range(100000):
    a = random.randint(-100000, 100000)
    b = random.randint(-100000, 100000)
    try:
        assert str(a + b) == addString2(str(a), str(b))
    except:
        print(a, b)

