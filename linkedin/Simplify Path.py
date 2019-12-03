class Solution:
    def simplifyPath(self, path: 'str') -> 'str':
        stack, res = [], ''
        for c in path.split('/'):
            if not c or c == '.': continue
            if c == '..':
                if stack: stack.pop()
            else: stack.append(c)
        for c in stack:
            res += '/' + c
        return res if res else '/'