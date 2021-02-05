import collections
# just need to find one path
def ladderLength(begin: str, end: str, words):
    dq = collections.deque([begin])
    words = set(words)
    if end not in words: return []
    if begin in words: words.remove(begin)
    seen = set()
    prev = {}
    while dq:
        sz = len(dq)
        for _ in range(sz):
            temp = dq.popleft()
            cur = list(temp)
            for i in range(len(cur)):
                c = cur[i]
                for sub in range(ord('a'), ord('z') + 1):
                    cur[i] = chr(sub)
                    nxt = ''.join(cur)
                    if nxt in words and nxt not in seen:
                        seen.add(nxt)
                        prev[nxt] = temp
                        if nxt == end:
                            res = [nxt]
                            while res[-1] in prev:
                                res.append(prev[res[-1]])
                            return res[::-1]
                        dq.append(nxt)
                cur[i] = c
    return []
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(ladderLength(beginWord, endWord, wordList))
