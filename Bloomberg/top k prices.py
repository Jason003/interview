'''
3. 获取top K报价
公司的报价信息图可以按照如下结构分类：

Finance — Bloomberg  [1000, 750, 640]
            |
            — Banking — BoA [800, 239]
            |               |
            |                — Chase [12, 5]
             — Advertising — …
非叶子结点表示公司类名 (Banking)。 其包含属于此分类的list of company ([BoA, Chase])，和子类的list ([Banking, Advertising])
叶子结点表示公司个体  (Bloomberg])。其包含一系列从大到小排好序的报价。
'''
import heapq
class Node:
    def __init__(self, name, children=None, prices=None):
        if prices is None:
            prices = []
        if children is None:
            children = []
        self.name = name
        self.children = children
        self.prices = prices

def getTopKPrices(root, name, k):
    def findNode(node):
        if not node: return None
        if node.name == name:
            return node
        for child in node.children:
            res = findNode(child)
            if res: return res
    node = findNode(root)
    heap = []
    def getPrices(node):
        if not node: return
        for price in node.prices:
            heapq.heappush(heap, price)
            if len(heap) > k:
                heapq.heappop(heap)
        for child in node.children:
            getPrices(child)
    getPrices(node)
    return heap

chase = Node('chase', [], [12, 5])
boa = Node('boa', [chase], [800, 239])
banking = Node('banking', [boa], [])
bb = Node('bb', [], [1000, 750, 640])
finance = Node('finance', [bb, banking], [])


print(getTopKPrices(finance, 'banking', 3))