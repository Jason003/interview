# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = collections.defaultdict(set)
        leaves = set()

        def inorder(node, prev):
            if node:
                if not node.left and not node.right:
                    leaves.add(node.val)
                inorder(node.left, node)
                if prev:
                    graph[prev.val].add(node.val)
                    graph[node.val].add(prev.val)
                inorder(node.right, node)

        inorder(root, None)
        if k in leaves: return k
        dq = collections.deque([k])
        seen = {k}
        while dq:
            sz = len(dq)
            for _ in range(sz):
                cur = dq.popleft()
                for nxt in graph[cur]:
                    if nxt in leaves: return nxt
                    if nxt not in seen:
                        seen.add(nxt)
                        dq.append(nxt)

