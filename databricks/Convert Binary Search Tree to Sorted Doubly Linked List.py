"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return root
        first, last = None, None
        def inorder(node):
            nonlocal first, last
            if node:
                inorder(node.left)
                if not first: first = node
                if last:
                    last.right, node.left = node, last
                last = node
                inorder(node.right)
        inorder(root)
        first.left, last.right = last, first
        return first