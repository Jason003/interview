class Solution:
    def countOfAtoms(self, f):
        """
        :type formula: str
        :rtype: str
        """
        coeff, cnt, elem, d, i, stack = 1, 0, '', collections.defaultdict(int), 0, []
        for c in f[::-1]:
            if c.isdigit():
                cnt += int(c) * (10 ** i)
                i += 1
            elif c == ')':
                stack.append(cnt)
                coeff *= cnt
                cnt, i = 0, 0
            elif c == '(':
                coeff //= stack.pop()
                cnt, i = 0, 0
            elif c.isupper():
                elem += c
                d[elem[::-1]] += coeff * cnt if cnt > 0 else coeff
                cnt, i, elem = 0, 0, ''
            elif c.islower():
                elem += c
        return ''.join([a + (str(b) if b > 1 else '') for a, b in sorted(d.items())])