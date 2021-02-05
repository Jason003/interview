'''
2. 压缩字符串
有两个服务器A，B。服务器A每天需要将一系列log发给B。每个log由一个string编号和一个string message连接组成，其中message可能包含ASCII码中所有可能的字符。

设计一个方案将log在A端压缩并在B端解压，并能复原log中的全部信息。
'''

def compress(string, id):

    res = ""

    count = 1

    #Add in first character
    res += string[0]

    #Iterate through loop, skipping last one
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count+=1
        else:
            if(count > 1):
                #Ignore if no repeats
                res += str(count)
            res += string[i+1]
            count = 1
    #print last one
    if(count > 1):
        res += str(count)
    return str(id) + res

def decompress(s):
    id = ''
    res = ''
    num = 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        else:
            if num != 0:
                if not res:
                    id = num
                else:
                    res += res[-1] * (num - 1)
            res += c
            num = 0
    if num != 0:
        res += res[-1] * (num - 1)
    return res, id
print(compress('aaaaaaaaaddddddddddddddddddddddddddddddddbffdafdfdafdafaf', 1))
print(decompress(compress('aaaaaaaaaddddddddddddddddddddddddddddddddbffdafdfdafdafaf', 1)))