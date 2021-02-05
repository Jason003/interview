'''
We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.
'''

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        # can only place A[i] to i - 1, i or i + 1
        return all(abs(a - i) <= 1 for i, a in enumerate(A))