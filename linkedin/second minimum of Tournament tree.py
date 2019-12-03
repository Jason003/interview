#
# * A tournament tree is a binary tree
# * where the parent is the minimum of the two children.
# * Given a tournament tree find the second minimum value in the tree.
# * A node in the tree will always have 2 or 0 children.
# * Also all leaves will have distinct and unique values.
# *         2
# *      /    \
# *     2      3
# *    / \    /  \
# *   4   2   5   3
# * 2,3,4,5
# * In this given tree the answer is 3.
'''
Basically, you are comparing all the winners except the first winner. That is why you need to go down it's direction and compare with the other members who haven't faced each other in the process.
Time complexity: O(log(N)) where N is the number of players.
Space complexity: O(log(N)) depth of the recusive stack
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

import collections
class Solution(object):
    def findSecondMinimumValue(self, root):
        if not root or not root.left or not root.right:
            return -1
        # for left and right sub-node, if their value is the same with the parent node value,
        # need to using recursion to find the next candidate, otherwise use their node value as the candidate.
        l, r = root.left.val, root.right.val
        if l == root.val:
            l = self.findSecondMinimumValue(root.left)
        if r == root.val:
            r = self.findSecondMinimumValue(root.right)
        if r != -1 and l != -1:
            return min(r, l)
        elif l == -1:
            return r
        else:
            return l

    def findKthMinimumValue(self, root, k):
        dq = collections.deque([root])
        seen = set()
        while dq:
            sz = len(dq)
            for _ in range(sz):
                curr = dq.popleft()
                seen.add(curr.val)
                if len(seen) == k:
                    return max(seen)
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
        return -1

root = Node(2)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(2)
root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(3)
print(Solution().findKthMinimumValue(root, 1))
print(Solution().findKthMinimumValue(root, 2))
print(Solution().findKthMinimumValue(root, 3))
print(Solution().findKthMinimumValue(root, 4))
print(Solution().findKthMinimumValue(root, 5))