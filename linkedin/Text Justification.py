class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # cur: containing words in current line, letterNum: sum of the words' lengths of current line
        res, cur, letterNum = [], [], 0
        for w in words:
            if len(w) + len(cur) + letterNum <= maxWidth:
                cur.append(w)
                letterNum += len(w)
            else:
                for i in range(maxWidth - letterNum):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur = [w]
                letterNum = len(w)
        finalLine = ' '.join(cur)
        finalLine += ' ' * (maxWidth - len(finalLine))
        res.append(finalLine) # add the final line
        return res