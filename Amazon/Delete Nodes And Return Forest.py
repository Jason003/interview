'''
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.



Example 1:



Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        d = set(to_delete)
        res = []
        def helper(node):
            if not node: return None
            if node.val in d:
                l, r = helper(node.left), helper(node.right)
                if l: res.append(node.left)
                if r: res.append(node.right)
                return None
            node.left, node.right = helper(node.left), helper(node.right)
            return node
        cur = helper(root)
        return res + [cur] if cur else res