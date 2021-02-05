def decodeString(s):
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
            curString = stack.pop() + curString * stack.pop() # first popped one is previous string, second poped one is the number
        elif c.isdigit():
            curNum = curNum * 10 + int(c)
        else:
            curString += c
    return curString