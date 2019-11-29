def replaceString(s, src, dst):
    res = []
    i = 0
    while i < len(s):
        if i + len(src) <= len(s) and s[i: i + len(src)] == src:
            res.append(dst)
            i += len(src)
        else:
            res.append(s[i])
            i += 1
    return ''.join(res)


print(replaceString('adsadadcf', 'ad', ''))
