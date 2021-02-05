class Solution:
    def __init__(self):
        self.map = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node in self.map: return self.map[node]
        self.map[node] = Node(node.val, [])
        for nei in node.neighbors:
            self.map[node].neighbors.append(self.cloneGraph(nei))
        return self.map[node]