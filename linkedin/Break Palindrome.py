def solution(s):
    s = list(s)
    n = len(s)
    for ch in range(26):
        new_c = chr(ord('a') + ch)
        for i, c in enumerate(s):
            if c != new_c and not (n % 2 == 1 and i == n // 2):
                s[i] = new_c
                return ''.join(s)
    return 'IMPOSSIBLE'

print(solution('zzz'))
