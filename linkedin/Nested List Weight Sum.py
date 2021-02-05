
'''
Instead of multiplying by depth, add integers multiple times (by going level by level and adding the unweighted sum to the weighted sum after each level).
'''
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(l, level):
            res = 0
            for ni in l:
                if ni.isInteger():
                    res += ni.getInteger() * level
                else:
                    res += dfs(ni.getList(), level + 1)
            return res
        return dfs(nestedList, 1)

    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def get_depth(ni):
            if ni.isInteger():
                return 1
            return 1 + max([get_depth(i) for i in ni.getList()] or [0])

        d = max([get_depth(i) for i in nestedList] or [0])

        def dfs(l, level):
            res = 0
            for ni in l:
                if ni.isInteger():
                    res += ni.getInteger() * (d - level)
                else:
                    res += dfs(ni.getList(), level + 1)
            return res

        return dfs(nestedList, 0)

    def depthSumInverse2(self, nestedList: List[NestedInteger]) -> int:
        unweighted = 0
        weighted = 0
        while nestedList:
            nextLevel = []
            for item in nestedList:
                if item.isInteger():
                    unweighted += item.getInteger()
                else:
                    nextLevel.extend(item.getList())
            weighted += unweighted
            nestedList = nextLevel
        return weighted