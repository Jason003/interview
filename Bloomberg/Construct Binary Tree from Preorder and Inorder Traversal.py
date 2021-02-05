class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(preStart, preEnd, inStart, inEnd, d, preorder, inorder):
            if preStart > preEnd or inStart > inEnd : return None
            res = TreeNode(preorder[preStart])
            dis = d[res.val] - inStart
            res.left = helper(preStart + 1, preStart + dis, inStart, inStart + dis - 1, d, preorder, inorder)
            res.right = helper(preStart + dis + 1, preEnd, inStart + dis + 1, inEnd, d, preorder, inorder)
            return res
        n = len(preorder)
        if not n: return None
        d = {}
        for i in range(0, n):
            d[inorder[i]] = i
        return helper(0, n - 1, 0, n - 1, d, preorder, inorder)

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(postStart, postEnd, inStart, inEnd, d, postorder, inorder):
            if postStart > postEnd or inStart > inEnd : return None
            res = TreeNode(postorder[postEnd])
            dis = d[res.val] - inStart
            res.left = helper(postStart, postStart + dis - 1, inStart, inStart + dis - 1, d, postorder, inorder)
            res.right = helper(postStart + dis, postEnd - 1, inStart + dis + 1, inEnd, d, postorder, inorder)
            return res
        n = len(postorder)
        if not n: return None
        d = {}
        for i in range(0, n):
            d[inorder[i]] = i
        return helper(0, n - 1, 0, n - 1, d, postorder, inorder)


    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        d = {}
        n = len(pre)
        for i, x in enumerate(post):
            d[x] = i
        def helper(pre, post, preStart, preEnd, postStart, postEnd):
            if preStart > preEnd or postStart > postEnd: return None
            root = TreeNode(pre[preStart])
            if preStart == preEnd: return root
            leftLength = d[pre[preStart + 1]] - postStart + 1
            root.left = helper(pre, post, preStart + 1, preStart + leftLength, postStart, postStart + leftLength - 1)
            root.right = helper(pre, post, preStart + 1 + leftLength, preEnd, postStart + leftLength, postEnd - 1)
            return root
        return helper(pre, post, 0, n - 1, 0, n - 1)