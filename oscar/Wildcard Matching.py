'''
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
'''



class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # O(m^2 * n) time, O(mn) space, TLE
        # m, n = len(s), len(p)
        # dp = [[False] * (n + 1) for _ in range(m + 1)]
        # dp[0][0] = True
        # for i in range(0, m + 1):
        #     for j in range(1, n + 1):
        #         if p[j - 1] == '*':
        #             flag = False
        #             for k in range(i, -1, -1):
        #                 if dp[k][j - 1]:
        #                     flag = True
        #                     break
        #             dp[i][j] |= flag
        #         else:
        #             dp[i][j] = i > 0 and dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')
        # return dp[m][n]

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            flag = False
            for i in range(m + 1):
                flag |= dp[i][j - 1]
                if p[j - 1] == '*':
                    dp[i][j] |= flag
                else:
                    dp[i][j] = i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '?') and dp[i - 1][j - 1]
        return dp[m][n]

'''
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
'''


class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [False] * (n + 1)
        for i in range(0, m + 1):
            pre = dp[0]
            dp[0] = True if i == 0 else False
            for j in range(1, n + 1):
                tep = dp[j]
                if p[j - 1] == '*':
                    dp[j] = j > 1 and (dp[j - 2] or i > 0 and (s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[j])
                else:
                    dp[j] = i > 0 and pre and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                pre = tep
        return dp[n]

        # m, n = len(s), len(p)
        # dp = [[False] * (n + 1) for _ in range(m + 1)]
        # dp[0][0] = True # dp[i][j] means whether s[:i] and p[:j] is equal or not
        # for i in range(0, m + 1):
        #     for j in range(1, n + 1):
        #         if p[j - 1] == '*':
        #             dp[i][j] = j > 1 and (dp[i][j - 2] or i > 0 and (s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i - 1][j])
        #         else:
        #             dp[i][j] = i > 0 and dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        # return dp[m][n]