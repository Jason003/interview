'''
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.



Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

'''
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        heap = [(nums[i][0], i, 0) for i in range(n)]
        heapq.heapify(heap)
        mx = max(heap)[0]
        minRange = mx - heap[0][0]
        res = [heap[0][0], mx]
        while len(heap) == n:
            v, i, j = heapq.heappop(heap)
            if j < len(nums[i]) - 1:
                heapq.heappush(heap, (nums[i][j + 1], i, j + 1))
                mx = max(mx, nums[i][j + 1])
            if len(heap) == n and mx - heap[0][0] < minRange:
                minRange = mx - heap[0][0]
                res = (heap[0][0], mx)
        return res