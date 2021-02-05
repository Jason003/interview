def solution(s):
    s = list(s)
    n = len(s)
    for ch in range(26):
        new_c = chr(ord('a') + ch)
        for i, c in enumerate(s):
            if c > new_c and not (n % 2 == 1 and i == n // 2):
                s[i] = new_c
                return ''.join(s)
    return 'IMPOSSIBLE'

print(solution('aba'))
def helper(s):
    n = len(s)
    if s == 'a' * n or n & 1 and {c for c in s[:n//2] + s[n//2+1:]} == {'a'}:
        return 'IMPOSSIBLE'
    for i, c in enumerate(s):
        if c != 'a':
            return s[:i] + 'a' + s[i+1:]
print(helper('aaba'))