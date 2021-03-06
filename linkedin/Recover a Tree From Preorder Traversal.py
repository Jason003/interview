'''
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.



Example 1:


Input: S = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack = []
        i = 0
        n = len(S)
        while i < n:
            level = 0
            val = ''
            while i < n and S[i] == '-':
                level += 1
                i += 1
            while i < n and S[i] != '-':
                val += S[i]
                i += 1
            while level < len(stack): stack.pop()
            node = TreeNode(int(val))
            if stack and not stack[-1].left: stack[-1].left = node
            elif stack and stack[-1].left: stack[-1].right = node
            stack.append(node)
        return stack[0]