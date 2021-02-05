class BSTIterator:

    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self.stack.pop()
        curr = res.right
        while curr:
            self.stack.append(curr)
            curr = curr.left
        return res.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0 and self.stack[-1] is not None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Same as BST Iterator I. We need a stack to collect all in-order nodes.
The only difference is that the tree is converted into a list.
Here, all left nodes will be our prev that we see in ListNodes. Similarly, all right nodes will be our next.
'''
class BSTIteratorII:

    def __init__(self, root: TreeNode):
        self.dummy = TreeNode()
        self.stack = []
        self.curr = self.dummy
        self._collect_mins(root)

    # // If there's no right and there's no node to append to the 'list', there's no next
    def hasNext(self) -> bool:
        return len(self.stack) > 0 or self.curr.right is not None

    # // Go forward. If no right, then we're at the end, append next node. Otherwise, just move forward
    def next(self) -> int:
        # // If there's no next then we must have a node ready in the Stack
        if not self.curr.right:
            nxt = self.stack.pop()

            # // Discover next mins and unlink
            self._collect_mins(nxt.right)
            nxt.right = None

            # // Append to 'list'
            self.curr.right = nxt
            nxt.left = self.curr
        self.curr = self.curr.right
        return self.curr.val

    # // If the 'list' is empty or we're at the first nodes, there is no prev
    def hasPrev(self) -> bool:
        return self.curr != self.dummy and self.curr.left != self.dummy

    # // If the 'list' is empty or we're at the first nodes, there is no prev
    def prev(self) -> int:
        self.curr = self.curr.left
        return self.curr.val

    # // Should only be called once per node
    def _collect_mins(self, node):
        while node:
            self.stack.append(node)
            node = node.left