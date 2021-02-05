# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = collections.defaultdict(set)

        def traverse(node, pre):
            if node:
                if pre:
                    graph[pre.val].add(node.val)
                    graph[node.val].add(pre.val)
                traverse(node.left, node)
                traverse(node.right, node)

        traverse(root, None)
        dq = collections.deque([(target.val, 0)])
        seen = {target.val}
        res = []
        while dq:
            curr, step = dq.popleft()
            if step == K: res.append(curr)
            if step > K: return res
            for nxt in graph[curr]:
                if nxt not in seen:
                    seen.add(nxt)
                    dq.append((nxt, step + 1))
        return res


