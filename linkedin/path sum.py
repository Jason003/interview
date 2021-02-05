# -*- coding: utf-8 -*-
# @Time : 2020/12/16 13:46
# @Author : Jiefan

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        if not root.left and not root.right and sum == root.val: return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    # find all the paths from root to leave that sum to 'sum'
    def pathSumII(self, root: TreeNode, sum: int) -> List[List[int]]:
        def helper(node, cur, l):
            if not node: return
            if not node.left and not node.right and sum == cur + node.val:
                res.append(l + [node.val])
                return
            helper(node.left, cur + node.val, l + [node.val])
            helper(node.right, cur + node.val, l + [node.val])
        res = []
        helper(root, 0, [])
        return res

    # find the number of paths whose sum is 'sum', and the path can start / end anywhere
    def pathSum(self, root: TreeNode, sum: int) -> int:
        preSum = collections.Counter()
        def helper(node, preSum, curSum):
            if not node: return 0
            curSum += node.val
            res = preSum[curSum - sum]
            preSum[curSum] += 1
            res += helper(node.left, preSum, curSum) + helper(node.right, preSum, curSum)
            preSum[curSum] -= 1
            return res
        preSum[0] = 1
        return helper(root, preSum, 0)