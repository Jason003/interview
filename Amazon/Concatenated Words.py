import functools


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words: return []
        words, wSet, res = sorted(words, key=lambda s: len(s)), set(), []

        @functools.lru_cache(None)
        def judge(word, idx):
            if idx == len(word) and word != "":
                return True
            if len(word) < len(words[0]) * 2: return False
            for i in range(idx + 1, len(word) + 1):
                cur = word[idx: i]
                if cur in wSet and cur != word and judge(word, i):
                    return True
            return False

        for word in words:
            if judge(word, 0):
                res.append(word)
            wSet.add(word)
        return res

