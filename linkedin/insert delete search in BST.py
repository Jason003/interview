# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BST:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        if root.val == key:
            if not root.left and not root.right: return None
            if not root.left: return root.right
            if not root.right: return root.left
            left = root.left
            right = root.right
            p = right
            while p.left:
                p = p.left
            p.left = left
            return right
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
