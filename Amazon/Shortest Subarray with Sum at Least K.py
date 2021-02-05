class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + A[i]
        res = float('inf')
        dq = collections.deque() # monotonously increasing
        for i, s in enumerate(preSum):
            while dq and s - preSum[dq[0]] >= K: res = min(res, i - dq.popleft())
            while dq and s <= preSum[dq[-1]]: dq.pop()
            dq.append(i)
        return -1 if res == float('inf') else res
