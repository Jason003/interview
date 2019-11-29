class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
    def __str__(self):
        return str(self.val)


def lca_parent(p, q):
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
