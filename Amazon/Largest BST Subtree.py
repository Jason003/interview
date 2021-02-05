'''
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10
   / \
  5  15
 / \   \
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-bst-subtree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
For each subtree, we return 4 elements.

the status of this subtree, 1 means it's empty, 2 means it's a BST, 0 means it's not a BST
size of this subtree (we only care about size of BST though)
the minimal value in this subtree
the maximal value in this subtree
'''
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        res = 0
        def helper(node): # return status of bst, size of bst, left bound and right bound
            nonlocal res
            if not node:
                return 1, 0, None, None
            ls, l, ll, lr = helper(node.left)
            rs, r, rl, rr = helper(node.right)
            if (ls == 2 and node.val > lr or ls == 1) and (rs == 2 and node.val < rl or rs == 1):
                res = max(res, l + r + 1)
                return 2, l + r + 1, ll if ll else node.val, rr if rr else node.val
            return 0, 0, None, None
        helper(root)
        return res