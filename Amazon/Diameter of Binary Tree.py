# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        def pathDown(node):
            if not node:
                return 0
            l, r = pathDown(node.left), pathDown(node.right)
            self.res = max(self.res, l + r)
            return max(l, r) + 1
        pathDown(root)
        return self.res