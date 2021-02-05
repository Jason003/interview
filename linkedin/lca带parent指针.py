# 问清楚是不是都在树上!
# if bst:
def lowestCommonAncestor(root, p, q):
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
# 正常LCA
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

# 有可能不在树上
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.cnt = 0
        def LCA(node):
            if not node: return node
            l, r = LCA(node.left), LCA(node.right)
            if p == node or q == node:
                self.cnt += 1
                return node
            if not l: return r
            if not r: return l
            return node
        res = LCA(root)
        print(self.cnt)
        return res if self.cnt == 2 else None

# 有 parent: intersection of 2 linked list
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a, b = p, q
        while a != b:
            a = a.parent if a else q
            b = b.parent if b else p
        return a

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
    def __str__(self):
        return str(self.val)


def lca_parent(p, q):
    # 问清楚是不是都在树上
    def getHeight(node):
        h = 0
        while node:
            node = node.parent
            h += 1
        return h

    h1, h2 = getHeight(p), getHeight(q)
    if h1 < h2:
        h1, h2 = h2, h1
        p, q = q, p
    while h1 > h2:
        if not p:
            return None
        p = p.parent
        h1 -= 1
    while p and q:
        if p == q:
            return p
        p = p.parent
        q = q.parent
    return None

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.left = b
b.parent = a
a.right = c
c.parent = a
b.left = d
d.parent = b
c.right = e
e.parent = c
print(lca_parent(e, c))
