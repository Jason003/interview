# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def helper(node):
            if not node:
                return '#'
            return str(node.val) + ',' + helper(node.left) + ',' + helper(node.right)

        return helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper(dq):
            cur = dq.popleft()
            if cur == '#':
                return None
            root = TreeNode(int(cur))
            root.left, root.right = helper(dq), helper(dq)
            return root

        return helper(collections.deque(data.split(',')))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

https: // aaronice.gitbooks.io / lintcode / trees / serialize - and -deserialize - n - ary - tree.html

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
'''
和 Serialize and Deserialize Binary Tree 很相似，同样可以用pre-order结合DFS来实现。
区别在于，在root value之后要append一个children count，这样才可以方便deserialize。
'''


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """

        if not root:
            return '#'
        res = []
        res.append(str(root.val) + ',')
        res.append(str(len(root.children)) + ',')
        for c in root.children:
            res.append(self.serialize(c) + ',')
        return ''.join(res).strip(',')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data == '#': return None
        dq = collections.deque(data.split(','))

        def dfs():
            if not dq: return None
            info = dq.popleft()
            root = Node(int(info), [])
            sz = dq.popleft()
            for _ in range(int(sz)):
                root.children.append(dfs())
            return root

        return dfs()