# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # bottom-up approach, O(n)
    def sortedListToBST(self, head):
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        self.node = head
        return self.convert(0, l-1)

    def convert(self, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        l = self.convert(start, mid-1)
        root = TreeNode(self.node.val)
        root.left = l
        self.node = self.node.next
        root.right = self.convert(mid+1, end)
        return root