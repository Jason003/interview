'''
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
'''

'''
Let's build a list of candidate answers for which the final answer must be one of those candidates. 
Afterwards, choosing from these candidates is straightforward.

If the final answer has the same number of digits as the input string S, 
then the answer must be the middle digits + (-1, 0, or 1) flipped into a palindrome. 
For example, 23456 had middle part 234, and 233, 234, 235 flipped into a palindrome 
yields 23332, 23432, 23532. Given that we know the number of digits, 
the prefix 235 (for example) uniquely determines the corresponding palindrome 23532, 
so all palindromes with larger prefix like 23732 are strictly farther away from S than 23532 >= S.

If the final answer has a different number of digits, 
it must be of the form 999....999 or 1000...0001, 
as any palindrome smaller than 99....99 or bigger than 100....001 will be farther away from S.
'''

class Solution:
    def nearestPalindromic(self, S: str) -> str:
        K = len(S)
        candidates = [str(10**k + d) for k in (K-1, K) for d in (-1, 1)]
        prefix = S[:(K+1)//2]
        P = int(prefix)
        for start in map(str, (P-1, P, P+1)):
            candidates.append(start + (start[:-1] if K%2 else start)[::-1])

        def delta(x):
            return abs(int(S) - int(x))

        ans = None
        for cand in candidates:
            if cand != S and not cand.startswith('00'):
                if (ans is None or delta(cand) < delta(ans) or
                        delta(cand) == delta(ans) and int(cand) < int(ans)):
                    ans = cand
        return ans