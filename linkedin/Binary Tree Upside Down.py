'''
Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.


The mentioned steps are done level by level, it is guaranteed that every node in the given tree has either 0 or 2 children.



Example 1:


Input: root = [1,2,3,4,5]
Output: [4,5,2,null,null,3,1]
'''


class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if root and root.left:
            res = self.upsideDownBinaryTree(root.left)
            root.left.left = root.right
            root.left.right = root
            root.left = None
            root.right = None
            return res
        else:
            return root


'''
public class Solution {
    public TreeNode UpsideDownBinaryTree(TreeNode root) {
        TreeNode curr = root;
        TreeNode prev = null;
        TreeNode next = null;
        TreeNode temp = null;
        
        while (curr != null) {
            next = curr.left;
            curr.left = temp;
            temp = curr.right;
            curr.right = prev;
            prev = curr;
            curr = next;
        }
        
        return prev;
    }
}

Just think about how you can save the tree information 
you need before changing the tree structure.
'''
