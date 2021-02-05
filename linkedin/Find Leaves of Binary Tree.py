import collections
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        depth = collections.defaultdict(list)
        def get_depth(node):
            if not node: return 0
            res = max(get_depth(node.left), get_depth(node.right)) + 1
            depth[res].append(node.val)
            return res
        get_depth(root)
        return list(depth.values())