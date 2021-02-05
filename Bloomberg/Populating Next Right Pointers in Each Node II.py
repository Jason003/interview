class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        p = dum = Node()
        res = root
        while root:
            p.next = root.left
            if p.next:
                p = p.next
            p.next = root.right
            if p.next:
                p = p.next
            root = root.next
            if not root:
                root, p = dum.next, dum
        return res