'''
Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)

Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.


Example 1:

Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
'''


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        for i in range(n - 1): A[i + 1] += A[i]
        l, m = A[L - 1], A[M - 1]
        res = A[M + L - 1]
        for i in range(L + M, n):
            m = max(m, A[i - L] - A[i - L - M])
            l = max(l, A[i - M] - A[i - L - M])
            res = max(res, A[i] - A[i - L] + m, A[i] - A[i - M] + l)
        return res
