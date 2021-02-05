class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # tree = collections.defaultdict(set)
        # wordList = set(wordList)
        # if endWord not in wordList: return []
        # bq, eq = {beginWord}, {endWord}
        # rev = False  # whether we change bq and eq
        # found = False
        # n = len(beginWord)
        # nq = set()
        # while bq and not found:
        #     wordList -= bq
        #     for cur in bq:
        #         for nxt in [cur[:i] + chr(c) + cur[i + 1:] for i in range(n) for c in range(ord('a'), ord('z') + 1)]:
        #             if nxt in wordList:
        #                 if nxt in eq:
        #                     found = True
        #                 else:
        #                     nq.add(nxt)
        #                 tree[nxt].add(cur) if rev else tree[cur].add(nxt)
        #     bq, nq = nq, set()
        #     if len(bq) > len(eq):
        #         bq, eq, rev = eq, bq, not rev
        #
        # def buildPath(x):
        #     return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in buildPath(y)]
        #
        # return buildPath(beginWord)

        # bfs
        dq = collections.deque([[beginWord]])
        wordList = set(wordList)
        if endWord not in wordList: return []
        if beginWord in wordList: wordList.remove(beginWord)
        res = []
        flag = False
        while dq:
            toRemove = set()
            sz = len(dq)
            for _ in range(sz):
                cur = dq.popleft()
                last = list(cur[-1])
                for i in range(len(last)):
                    org = last[i]
                    for c in range(ord('a'), ord('z') + 1):
                        last[i] = chr(c)
                        newWord = ''.join(last)
                        if newWord in wordList:
                            if newWord == endWord:
                                res.append(cur + [newWord])
                                flag = True
                            toRemove.add(newWord)
                            dq.append(cur + [newWord])
                    last[i] = org
            wordList -= toRemove
            if flag: return res
        return res
