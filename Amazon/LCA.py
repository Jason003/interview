
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        l, r = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        if not l:
            return r
        if not r:
            return l
        return root

def LCA(root, a, b):
    parent = {}
    depth = {}
    def getParent(node, pre, d):
        if node:
            parent[node] = pre
            depth[node] = d
            for child in node.children:
                getParent(child, node, d + 1)
    getParent(root, None, 0)
    def getLCA(a, b):
        if not a or not b: return None
        if a == b: return a
        if depth[a] > depth[b]: return getLCA(parent[a], b)
        elif depth[a] < depth[b]: return getLCA(a, parent[b])
        else: return getLCA(parent[a], parent[b])
    return getLCA(a, b)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)

a.children = [b, c]
b.children = [d, e, f]
print(LCA(a, c, d).val)


