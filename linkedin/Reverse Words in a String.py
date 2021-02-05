
def reverseWords(s: str) -> str:
    # return ' '.join(s.split()[::-1])

    def reverse(s, lo, hi):
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1

    s = list(s)
    n = len(s)
    reverse(s, 0, n - 1)
    idx = 0 # if words might be divided by more than one space
    i = 0
    while i < n:
        if s[i] != ' ':
            if idx != 0:
                s[idx] = ' '
                idx += 1
            j = i
            while j < n and s[j] != ' ':
                s[idx] = s[j]
                idx += 1
                j += 1
            reverse(s, idx - (j - i), idx - 1)
            i = j + 1
        else:
            i += 1
    return ''.join(s[:idx])
print(reverseWords('     ewqeq       ewqeqwee         '))
