class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n <= 1: return []
        fs = [i for i in range(2, n // 2 + 1) if n % i == 0]
        res = []
        def dfs(curr, num, idx):
            if num == 1:
                res.append(curr)
            for i in range(idx, len(fs)):
                if num % fs[i] == 0:
                    dfs(curr + [fs[i]], num // fs[i], i)
        dfs([], n, 0)
        return res
'''
formula 1: time = (the number of nodes in the recursive tree) * (the time each node takes up)
formula 2: the number of nodes in the recursive tree  = 
                 (the most number of branches among each node) ^ (the height of the tree)
For the number of branches, it has at most N (from 2 to n) and in terms of the height of the tree, it should be logN since when the given number n is only decomposed by 2 will lead to the solution which has the longest length (pls take 32 as example in the description page). Thus, the number of nodes = (N)^(logN). And since each node only takes up O(1) time, therefore, the total time should be O(N^(logN))

Space complexity: O(logN)
Things will cost EXTRA space:
1. the number of call stacks invoked = the height of the recursive tree = logN
2. the item used to store the current solution which takes up logN at most (again, when the input n is only decomposed by 2)

Alright, hopefully, my explns help :) and if you find any flaws in my explns above, pls point that out and I will appreciate so much.
'''