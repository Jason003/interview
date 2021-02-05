'''
Distance(X, Y) = Distance(root, X) +Distance(root, Y) — 2*(Distance(root to LCA(X,Y)
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def distance(root, x, y):
    if not root or not x or not y: return -1
    def lca(root, x, y):
        if not root or root == x or root == y:
            return root
        l, r = lca(root.left, x, y), lca(root.right, x, y)
        if not l: return r
        if not r: return l
        return root

    def dis(root, x):
        if root == x: return 0
        if not root: return -1
        l, r = dis(root.left, x), dis(root.right, x)
        if l != -1: return l + 1
        if r != -1: return r + 1
        return -1
    dis1 = dis(root, x)
    dis2 = dis(root, y)
    if dis1 == -1 or dis2 == -1: return -1
    lca_node = lca(root, x, y)
    return dis1 + dis2 - 2 * dis(root, lca_node)

a = Node(1)
b = Node(1)
c = Node(1)
d = Node(1)
e = Node(1)
f = Node(1)
a.left, a.right = b, c
b.left, b.right = d, e
d.left = f
print(distance(a, c, d))
