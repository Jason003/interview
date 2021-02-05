class Solution:
    def largestBSTSubtree(self, root) -> int:
        def helper(root): # return smallest value in the subtree, biggest value in the subtree, number of nodes in the subtree
            if not root:
                return float("inf"), float("-inf"),0 # return it to make sure the its parent is always valid
            l_min,l_max,lv=helper(root.left)
            r_min,r_max,rv=helper(root.right)
            if l_max<root.val<r_min:
                return min(root.val,l_min),max(root.val,r_max),lv+rv+1
            return float("-inf"), float("inf"),max(lv,rv) # return it to make sure the its parent is always invalid
        return helper(root)[2]
'''
when we want to determine if a tree is bst:
the largest value in the left < node.val < the smallest value in the right 
'''
