# given a string, return the depth of it
def depth(s):
    l = res = 0
    for c in s:
        if c == '(':
            l += 1
        elif c == ')':
            l -= 1
        if l < 0: return -1
        res = max(res, l)
    return res if l == 0 else -1




# how to return the deepest substring
def depth2(s):
    l = 0
    res = []
    curr = ''
    deep = 0
    for i, c in enumerate(s):
        if c == '(':
            l += 1
            curr = ''
        elif c == ')':
            if l == deep:
                res.append(curr)
            elif l > deep:
                res = [curr]
            l -= 1
            curr = ''
        else:
            curr += c
        deep = max(deep, l)
        if l < 0: return []
    return res if l == 0 else []

print(depth2('((aaa(dddd(eeee)))(((ffff))bbb(ccc)))'))