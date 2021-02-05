'''
首先是如果是在string里的-，比如

input:
SELECT * FROM users --users table selected
WHERE users.name="-David" --user name select

output:
SELECT * FROM user
WHERE users.name="-David"

这个还是好的，然后他出了一个比较tricky的：

就是比如有“\"的情况，这种情况如果你的代码里写是有问题的：比如是if s=="\"，是会报错的，因为“\"这个字符是escape字符。正确的方法是写成if s=="\\".

不知道这个trick。面试半个小时后直接收到据信。大家准备的时候注意下这种情况。
'''
def removeComments(sql):
    lists = sql.split('\n')
    res = []
    for m, s in enumerate(lists):
        temp = ''
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i] == s[i + 1] == '-':
                i += 2
                break
            temp += s[i]
            i += 1
        if temp != '':
            res.append(temp)
    return '\n'.join(res)

def removeComments2(sql):
    lists = sql.split('\n')
    quoted = False
    res = []
    for m, s in enumerate(lists):
        temp = ''
        i = 0
        while i < len(s):
            if s[i] == '"':
                quoted = not quoted
            elif s[i] == '\\':
                if i + 1 < len(s):
                    temp += s[i : i + 2]
                i += 2
                continue
            else:
                if not quoted and i < len(s) - 1 and s[i] == s[i + 1] == '-':
                    i += 2
                    break
            temp += s[i]
            i += 1
        if temp != '':
            res.append(temp)
    return '\n'.join(res)

print(removeComments(
'''SELECT * FROM files -- This is an inline comment\n WHERE fullpath LIKE "/home/\\' --";'''
))