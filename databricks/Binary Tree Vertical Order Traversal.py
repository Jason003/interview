class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution:
    def verticalOrder(self, root: TreeNode): # O(n) space & time
        if not root: return []
        d = collections.defaultdict(list)
        mx, mn = -float('inf'), float('inf')
        dq = collections.deque([(root, 0)])
        while dq:
            curr, idx = dq.popleft()
            d[idx].append(curr.val)
            mx = max(mx, idx)
            mn = min(mn, idx)
            if curr.left:
                dq.append((curr.left, idx - 1))
            if curr.right:
                dq.append((curr.right, idx + 1))
        return [d[i] for i in range(mn, mx + 1)]