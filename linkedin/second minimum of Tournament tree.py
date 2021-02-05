#
# * A tournament tree is a binary tree
# * where the parent is the minimum of the two children.
# * Given a tournament tree find the second minimum value in the tree.
# * A node in the tree will always have 2 or 0 children.
# * Also all leaves will have distinct and unique values.
# *         1
# *      /    \
# *     1      3
# *    / \
# *   1   2
# * 2,3,4,5
# * In this given tree the answer is 3.
'''
Basically, you are comparing all the winners except the first winner. That is why you need to go down it's direction and compare with the other members who haven't faced each other in the process.
Time complexity: O(log(N)) where N is the number of players.
Space complexity: O(log(N)) depth of the recusive stack
'''
import heapq

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
        heap = []
        seen = set()
        def dfs(node):
            if node:
                dfs(node.left)
                if node.val not in seen:
                    seen.add(node.val)
                    heapq.heappush(heap, -node.val)
                    if len(heap) > k: heapq.heappop(heap)
                dfs(node.right)
        dfs(root)
        return -heap[0]


root = Node(1)
root.left = Node(1)
root.left.left = Node(1)
root.left.right = Node(2)
root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(3)
print(Solution().findKthMinimumValue(root, 1))
print(Solution().findKthMinimumValue(root, 2))
print(Solution().findKthMinimumValue(root, 3))
print(Solution().findKthMinimumValue(root, 4))
print(Solution().findKthMinimumValue(root, 5))