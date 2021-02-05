'''
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.
'''
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        return sum(((len(arr) - i) * (i + 1) + 1) // 2 * arr[i] for i in range(len(arr)))