import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        res = []
        # monotone deque storing indexes, decreasing
        for i, num in enumerate(nums):
            while dq and num > nums[dq[-1]]: dq.pop()
            dq.append(i)
            if i - dq[0] >= k: dq.popleft()
            if i >= k - 1: res.append(nums[dq[0]])
        return res