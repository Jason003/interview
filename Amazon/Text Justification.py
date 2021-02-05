class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # cur: containing words in current line, letterNum: sum of the words' lengths of current line
        res, cur, letterNum = [], [], 0
        for w in words:
            if len(w) + len(cur) + letterNum > maxWidth:
                for i in range(maxWidth - letterNum): cur[i % (len(cur) - 1 or 1)] += ' '
                res, cur, letterNum = res + [''.join(cur)], [], 0
            cur, letterNum = cur + [w], letterNum + len(w)
        return res + [' '.join(cur).ljust(maxWidth)] # add the final line