'''
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
'''

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        cnt = collections.Counter(s)
        for c, v in cnt.items():
            if v < k:
                return max([self.longestSubstring(sub, k) for sub in s.split(c) if len(sub) >= k] or [0])
        return len(s)