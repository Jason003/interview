import collections

def maxSlidingWindow(nums, k: int):
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


def minSlidingWindow(nums, k: int):
    dq = collections.deque()
    res = []
    for i, num in enumerate(nums):
        while dq and num < nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        if dq and i - dq[0] >= k:
            dq.popleft()
        if i >= k - 1: res.append(nums[dq[0]])
    return res

print(minSlidingWindow([1,2,1,4,5,6,7], 2))