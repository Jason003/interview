def break_word(s, words):
    words = set(words)
    lengths = set(map(len, words))

    def dfs(idx):
        if idx == len(s):
            return True, ''
        for i in range(idx, len(s)):
            for length in lengths:
                word = s[i: i + length]
                if word in words:
                    temp = dfs(i + length)
                    if temp[0]:
                        return True, word + ' ' + temp[1]
        return False, ''

    res = dfs(0)
    if res[0]:
        return res[1]
    else:
        return None


def trim(s):
    n = len(s)
    l, r = 0, len(s) - 1
    while l < n and s[l] == ' ':
        l += 1
    while r >= 0 and s[r] == ' ':
        r -= 1
    print(l, r)
    return s[l: r + 1]


print(len(trim('       ')))
