import heapq
def topK1(A, k):
    # O(nlogn)
    if len(A) < k:
        return []
    return sorted(A)[-k:]

def topK2(A, k):
    # O(nlogk)
    if len(A) < k:
        return []
    heap = []
    for a in A:
        heapq.heappush(heap, a)
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted(heap)

def topK3(A, k):
    # O(n) if we don't need to sort, otherwise, it is O(n + klogk)
    if len(A) < k:
        return []
    def quickSelect(nums, l, r, k):
        p = l
        for i in range(l, r):
            if nums[i] <= nums[r]:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        if p == k:
            return p
        elif p < k:
            return quickSelect(nums, p + 1, r, k)
        else:
            return quickSelect(nums, l, p - 1, k)
    idx = quickSelect(A, 0, len(A) - 1, len(A) - k)
    return sorted(A[idx:])

import random
for i in range(100):
    A = [random.randint(0, 100) for _ in range(100)]
    K = random.randint(1, 100)
    assert topK1(A, K) == topK2(A, K) == topK3(A, K)