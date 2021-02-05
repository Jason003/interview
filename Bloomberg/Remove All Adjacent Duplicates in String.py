'''
Remove all the chars which appear for >=k times continuously
e.g.
s = "deeedbbcccbdaaaa", k = 3
return ""

if just remove those = k times, we don't need to use 'removed' variable
'''
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        removed = None
        for c in s:
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
            else:
                if c != removed:
                    stack.append([c, 1])
                    removed = None
            if stack and stack[-1][1] == k:
                removed = stack.pop()[0]
        return ''.join(i * j for i, j in stack)
print(Solution().removeDuplicates('aabbcccbbd', 3))