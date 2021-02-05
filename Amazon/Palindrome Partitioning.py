'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution:
    def partition(self, s: 'str') -> 'List[List[str]]':
        def judge(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]: return False
                i, j = i + 1, j - 1
            return True
        if not s: return [[]]
        res, n = [], len(s)
        for i in range(1, n + 1):
            if judge(s[:i]):
                res += [[s[:i]] + r for r in self.partition(s[i:])]
        return res
'''
Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i - 1 for i in range(n + 1)]
        for i in range(n):
            j = 0
            while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
                dp[i + j + 1] = min(dp[i + j + 1], dp[i - j] + 1)
                j += 1
            j = 1
            while i - j + 1 >= 0 and i + j < n and s[i - j + 1] == s[i + j]:
                dp[i + j + 1] = min(dp[i + j + 1], dp[i - j + 1] + 1)
                j += 1
        return dp[n]