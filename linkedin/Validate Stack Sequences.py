class Solution:
    def validateStackSequences(self, pushed: 'List[int]', popped: 'List[int]') -> 'bool':
        if not pushed and not popped: return True
        n, stack, idx = len(pushed), [], 0
        for i in range(n + 1):
            if not stack: stack.append(pushed[i])
            else:
                while stack and stack[-1] == popped[idx]:
                    stack.pop()
                    idx += 1
                if i < n: stack.append(pushed[i])
        return not stack and idx == n