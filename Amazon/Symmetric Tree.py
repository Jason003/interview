# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # def judge(a, b):
        #     if not a and not b: return True
        #     if not a and b or not b and a or a.val != b.val: return False
        #     return judge(a.left, b.right) and judge(a.right, b.left)
        # if not root: return True
        # return judge(root.left, root.right)

        if not root: return True
        stack = [(root.left, root.right)]
        while stack:
            cur = stack.pop()
            l, r = cur[0], cur[1]
            if not l and not r: continue
            if not l and r or not r and l or l.val != r.val: return False
            stack.append((l.right, r.left))
            stack.append((l.left, r.right))
        return True
