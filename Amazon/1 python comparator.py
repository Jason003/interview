from functools import cmp_to_key

def cmp(x, y):
    return int(x) - int(y)

print(sorted(['111','22',], key = cmp_to_key(cmp)))
print(sorted(['111','22',]))