class TreeNode:
    def __init__(self, val, selected=False):
        self.val = val
        self.selected = selected
        self.children = []
    def __str__(self):
        return str(self.val) + ' ' + str(self.children)
    def __repr__(self):
        return str(self.val) + ' ' + str(self.children)

def getNewTree(root):
    res = TreeNode(-1)
    def traverse(node, pre):
        if node:
            if node.selected:
                add = TreeNode(node.val, True)
                pre.children.append(add)
            for child in node.children:
                traverse(child, pre if not node.selected else add)

    traverse(root, res)
    return res.children

a = TreeNode(1, True)
b = TreeNode(2, True)
c = TreeNode(3, False)
d = TreeNode(4, True)
c.children = [d]
a.children = [b, c]

for i in getNewTree(a):
    print(i)