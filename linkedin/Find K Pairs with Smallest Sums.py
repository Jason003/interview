import heapq

def kSmallestPairs(nums1, nums2, k: int):
    # ask if there are negative numbers, if so, we need to use heap + brute-traverse
    m, n = len(nums1), len(nums2)
    if m == 0 or n == 0: return []
    res, heap, seen = [], [(nums1[0] * nums2[0], 0, 0)], {(0, 0)}
    for _ in range(k): # O(klogk)
        if not heap: return res
        v, i, j = heapq.heappop(heap)
        res.append((nums1[i], nums2[j]))
        if i < m - 1 and (i + 1, j) not in seen:
            seen.add((i + 1, j))
            heapq.heappush(heap, (nums1[i + 1] * nums2[j], i + 1, j))
        if j < n - 1 and (i, j + 1) not in seen:
            seen.add((i, j + 1))
            heapq.heappush(heap, (nums1[i] * nums2[j + 1], i, j + 1))
    return res
print(kSmallestPairs([1,2,3,4,5],[2,3,4,5,6],10))