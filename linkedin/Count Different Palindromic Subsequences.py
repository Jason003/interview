'''
Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo 10^9 + 7.

A subsequence of a string S is obtained by deleting 0 or more characters from S.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

Example 1:
Input:
S = 'bccb'
Output: 6
Explanation:
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
'''


class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        n = len(S)
        cache = {}
        mod = 10 ** 9 + 7

        def helper(i, j):
            if i > j: return 0
            if i == j: return 1
            if (i, j) in cache: return cache[i, j]
            if S[i] != S[j]:
                cache[i, j] = (helper(i + 1, j) + helper(i, j - 1) - helper(i + 1, j - 1)) % mod
            else:
                l, r = i + 1, j - 1
                while l < j and S[l] != S[i]: l += 1
                while r > i and S[r] != S[j]: r -= 1
                if l > r:
                    '''
                       // consider the string from i to j is "a...a" "a...a"... where there is no character 'a' inside the leftmost and rightmost 'a'
                       /* eg:  "aba" while i = 0 and j = 2:  dp[1][1] = 1 records the palindrome{"b"}, 
                         the reason why dp[i + 1][j  - 1] * 2 counted is that we count dp[i + 1][j - 1] one time as {"b"}, 
                         and additional time as {"aba"}. The reason why 2 counted is that we also count {"a", "aa"}. 
                         So totally dp[i][j] record the palindrome: {"a", "b", "aa", "aba"}. 
                         */ 
                    '''
                    cache[i, j] = (helper(i + 1, j - 1) * 2 + 2) % mod
                elif l == r:
                    '''
                    // consider the string from i to j is "a...a...a" where there is only one character 'a' inside the leftmost and rightmost 'a'
                       /* eg:  "aaa" while i = 0 and j = 2: the dp[i + 1][j - 1] records the palindrome {"a"}.  
                         the reason why dp[i + 1][j  - 1] * 2 counted is that we count dp[i + 1][j - 1] one time as {"a"}, 
                         and additional time as {"aaa"}. the reason why 1 counted is that 
                         we also count {"aa"} that the first 'a' come from index i and the second come from index j. So totally dp[i][j] records {"a", "aa", "aaa"}
                        */
                    '''
                    cache[i, j] = (helper(i + 1, j - 1) * 2 + 1) % mod
                else:
                    '''
                    // consider the string from i to j is "a...a...a... a" where there are at least two character 'a' close to leftmost and rightmost 'a'
                       /* eg: "aacaa" while i = 0 and j = 4: the dp[i + 1][j - 1] records the palindrome {"a",  "c", "aa", "aca"}. 
                          the reason why dp[i + 1][j  - 1] * 2 counted is that we count dp[i + 1][j - 1] one time as {"a",  "c", "aa", "aca"}, 
                          and additional time as {"aaa",  "aca", "aaaa", "aacaa"}.  Now there is duplicate :  {"aca"}, 
                          which is removed by deduce dp[low + 1][high - 1]. So totally dp[i][j] record {"a",  "c", "aa", "aca", "aaa", "aaaa", "aacaa"}
                          */
                    '''
                    cache[i, j] = (helper(i + 1, j - 1) * 2 - helper(l + 1, r - 1)) % mod
            return cache[i, j]

        return helper(0, n - 1)

        # dp = [[0] * n for _ in range(n)] # dp[i][j] is the number of different Palindromic sequences in S[i:j+1]
        # mod = 10 ** 9 + 7
        # for i in range(n):
        #     dp[i][i] = 1
        # for i in range(n - 1, -1, -1):
        #     for j in range(i + 1, n):
        #         if S[i] == S[j]:
        #             lo, hi = i + 1, j - 1
        #             while lo < j and S[lo] != S[i]: lo += 1
        #             while hi > i and S[hi] != S[j]: hi -= 1
        #             if lo > hi: dp[i][j] = (dp[i + 1][j - 1] * 2 + 2) % mod
        #             elif lo == hi: dp[i][j] = (dp[i + 1][j - 1] * 2 + 1) % mod
        #             else: dp[i][j] = (dp[i + 1][j - 1] * 2 - dp[lo + 1][hi - 1]) % mod
        #         else:
        #             dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % mod
        # return dp[0][n - 1] % mod


def findPalindromicSubsequences(S: str) -> int:
    n = len(S)
    cache = {}

    def helper(i, j):
        if i > j: return set()
        if i == j: return {S[i]}
        if (i, j) in cache: return cache[i, j]
        if S[i] != S[j]:
            cache[i, j] = helper(i + 1, j) | helper(i, j - 1) - helper(i + 1, j - 1)
        else:
            cache[i, j] = {S[i], S[i] * 2} | {S[i] + s + S[i] for s in helper(i + 1, j - 1)} | helper(i + 1, j - 1)
        return cache[i, j]

    return helper(0, n - 1)

print(findPalindromicSubsequences('bccb'))