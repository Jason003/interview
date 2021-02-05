words = ['11','22','3333','4444','5555555']
maxLen = 10
def wordWrap(words, maxLen):
    res = []
    i = 0
    while i < len(words):
        remain = maxLen
        j = i
        while j < len(words):
            if remain - len(words[j]) < 0:
                break
            remain -= len(words[j]) + 1
            j += 1
        res.append('-'.join(words[i : j]))
        i = j
    return res
print(wordWrap(words, maxLen))


def fullJustify(lines, maxWidth):
    # cur: containing words in current line, letterNum: sum of the words' lengths of current line
    words = []
    for l in lines:
        words += l.split()
    res, cur, letterNum = [], [], 0
    for w in words:
        if len(w) + len(cur) + letterNum > maxWidth:
            for i in range(maxWidth - letterNum):
                cur[i % (len(cur) - 1 or 1)] += '-'
            res, cur, letterNum = res + [''.join(cur)], [], 0
        cur, letterNum = cur + [w], letterNum + len(w)
    if not cur: return res
    if len(cur) == 1: return res + cur
    for i in range(maxWidth - letterNum):
        cur[i % (len(cur) - 1 or 1)] += '-'
    return res + [''.join(cur)]

lines = [ "The day began as still as the",
          "night abruptly lighted with",
          "brilliant" ]
print(fullJustify(lines, 24))