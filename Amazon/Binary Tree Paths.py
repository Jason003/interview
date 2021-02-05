class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]
        res = []
        for s in self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right):
            res.append(str(root.val) + "->" + s)
        return res

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def dfs(node, curr):
            if not node: return
            if node and not node.left and not node.right:
                res.append('->'.join(map(str, curr + [node.val])))
                return
            dfs(node.left, curr + [node.val])
            dfs(node.right, curr + [node.val])
        dfs(root, [])
        return res