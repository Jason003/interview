'''
Follow up如果我给了你一个dict里面有一些String，小哥说要求还是character 的combination但是要求在dict里面，能不能时间复杂度要好一些
'''
class Solution:
    def letterCombinations(self, digits: 'str'):
        d, res = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}, []
        def dfs(idx, s):
            if idx == len(digits):
                res.append(s)
                return
            for c in d[digits[idx]]:
                dfs(idx + 1, s + c)
        if not digits: return []
        dfs(0, '')
        return res