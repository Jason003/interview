# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> None:
        if not preorder: return None
        i = 0
        def helper(bound):
            nonlocal i
            if i == len(preorder) or preorder[i] > bound:
                return None
            root = TreeNode(preorder[i])
            i += 1
            root.left = helper(root.val)
            root.right = helper(bound)
            return root
        return helper(float('inf'))

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        n = len(preorder)
        greater = [-1] * n
        stack = []
        for i, num in enumerate(preorder):
            while stack and num > preorder[stack[-1]]:
                greater[stack.pop()] = i
            stack.append(i)
        def helper(l, r):
            if l > r: return None
            root = TreeNode(preorder[l])
            root.left = helper(l + 1, greater[l] - 1 if greater[l] != -1 else r)
            root.right = helper(greater[l], r) if greater[l] != -1 else None
            return root
        return helper(0, n - 1)