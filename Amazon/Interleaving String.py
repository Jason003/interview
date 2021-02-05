'''
Given s1, s2, and s3, find whether s3 is formed by the interleaving of s1 and s2.



Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
'''

class Solution:
    def isInterleave(self, s1, s2, s3):
        r, c, l= len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        dp = [[True for _ in range(c+1)] for _ in range(r+1)]
        for i in range(r+1):
            for j in range(c+1):
                if i == j == 0: continue
                dp[i][j] = (i > 0 and dp[i-1][j] and s1[i-1] == s3[i-1+j]) or (j > 0 and dp[i][j-1] and s2[j-1] == s3[i-1+j])
        return dp[-1][-1]