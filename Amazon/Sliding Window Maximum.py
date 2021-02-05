import heapq, collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))
            while heap and i - heap[0][1] >= k:
                heapq.heappop(heap)
            if i >= k - 1: res.append(-heap[0][0])
        return res

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        res = []
        for i, num in enumerate(nums):
            while dq and num > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if dq and i - dq[0] >= k:
                dq.popleft()
            if i >= k - 1: res.append(nums[dq[0]])
        return res