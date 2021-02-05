'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def robIII(self, root: TreeNode) -> int:
        def helper(node):  # return max money if rob node, max money if not rob node
            if not node: return 0, 0
            l, r = helper(node.left), helper(node.right)
            return node.val + l[1] + r[1], max(l) + max(r)

        return max(helper(root))

    # You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
    def robII(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def helper(nums):
            nr, r = 0, 0 # not rob, rob
            for num in nums:
                nr, r = max(nr, r), nr + num
            return max(nr, r)
        return max(helper(nums[1:]), helper(nums[:-1]))
