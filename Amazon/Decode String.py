class Solution:
    def decodeString(self, s: 'str') -> 'str':
        stack = []
        curString = ''
        curNum = 0
        for c in s:
            if c == '[':
                stack.append(curNum)
                stack.append(curString)
                curString = ''
                curNum = 0
            elif c == ']':
                curString = stack.pop() + curString * stack.pop()
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curString += c
        return curString



