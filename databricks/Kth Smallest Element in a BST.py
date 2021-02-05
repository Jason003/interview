def kthSmallest(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right

class Solution:
    def kthSmallest(self, root, k):
        self.count = 0
        def inorder(node):
            if not node: return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.res = node.val
                return
            inorder(node.right)
        inorder(root)
        return self.res