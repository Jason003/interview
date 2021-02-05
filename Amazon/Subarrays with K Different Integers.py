'''
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.
'''

import collections
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        # calculate the amount of subarrays containing at most k different integers
        def helper(k):
            cnt, start, end, res = collections.Counter(), 0, 0, 0
            while end < len(A):
                if cnt[A[end]] == 0: k -= 1
                cnt[A[end]] += 1
                while start <= end and k < 0:
                    cnt[A[start]] -= 1
                    if cnt[A[start]] == 0: k += 1
                    start += 1
                res += end - start + 1
                end += 1
            return res

        return helper(K) - helper(K - 1)

