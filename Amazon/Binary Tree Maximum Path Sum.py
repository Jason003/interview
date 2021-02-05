# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -float('inf')
        def maxPathDown(node):
            if not node: return 0
            l, r = maxPathDown(node.left), maxPathDown(node.right)
            self.res = max(self.res, node.val + max(l, 0) + max(r, 0))
            return max(l, r, 0) + node.val
        maxPathDown(root)
        return self.res