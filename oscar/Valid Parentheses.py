class Solution:
    def isValid(self, s: 'str') -> 'bool':
        stack, d = [], {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in d.keys():
                stack.append(c)
            else:
                if not stack or stack[-1] not in d.keys() or d[stack[-1]] != c:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
