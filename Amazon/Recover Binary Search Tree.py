'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.a, self.b = None, None
        self.pre = None
        def inorder(node):
            if node:
                inorder(node.left)
                if self.pre and node.val < self.pre.val:
                    self.a = self.a if self.a else self.pre
                    self.b = node
                self.pre = node
                inorder(node.right)
        inorder(root)
        self.a.val, self.b.val = self.b.val, self.a.val