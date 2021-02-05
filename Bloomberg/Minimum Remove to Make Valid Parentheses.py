class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l, r = [], []
        for i, c in enumerate(s):
            if c == '(':
                l.append(i)
            elif c == ')':
                if l:
                    l.pop()
                else:
                    r.append(i)
        toRemove = set(l + r)
        return ''.join(s[i] for i in range(len(s)) if i not in toRemove)