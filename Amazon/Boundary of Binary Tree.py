'''
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.  (The values of the nodes may still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        res = []
        if not root: return res

        def isLeaf(node):
            return node != None and node.left == None and node.right == None

        if not isLeaf(root):
            res.append(root.val)
        left = root.left
        while left:
            if not isLeaf(left):
                res.append(left.val)
            if left.left:
                left = left.left
            else:
                left = left.right

        def addLeaves(node):
            if node:
                if isLeaf(node):
                    res.append(node.val)
                    return
                addLeaves(node.left)
                addLeaves(node.right)

        addLeaves(root)
        rights = []
        right = root.right
        while right:
            if not isLeaf(right):
                rights.append(right.val)
            if right.right:
                right = right.right
            else:
                right = right.left
        return res + rights[::-1]