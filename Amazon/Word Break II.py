class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        mem = {}
        def helper(idx):
            if idx == len(s):
                return ['']
            if idx in mem:
                return mem[idx]
            res = []
            for w in wordDict:
                length = len(w)
                if s[idx : idx + length] == w:
                    res.extend([(w + ' ' + rem).strip() for rem in helper(idx + length)])
            mem[idx] = res
            return res
        return helper(0)

'''
Word Break I
'''
class Solution:
    def wordBreak(self, s: str, wordList: List[str]) -> bool:
        lengths = set(map(len, wordList))
        wordList = set(wordList)

        def helper(i):
            if i == len(s):
                return True
            if i in mem:
                return mem[i]
            for length in lengths:
                if i + length <= len(s) and s[i: i + length] in wordList and helper(i + length):
                    mem[i] = True
                    return True
            mem[i] = False
            return False

        mem = {}
        return helper(0)