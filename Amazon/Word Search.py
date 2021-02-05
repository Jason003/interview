class Solution:
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        def helper(x, y, idx):
            nonlocal board
            if idx == len(word): return True
            if x >= m or y >= n or x < 0 or y < 0 or board[x][y] != word[idx]: return False
            c = board[x][y]
            board[x][y] = '#'
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if helper(x + dx, y + dy, idx + 1): return True
            board[x][y] = c
            return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if helper(i, j, 0): return True
        return False

'''
follow up: if we need to determine for a list of words
'''
'''
let:
N = num of rows
M = num of columns
X = number of words in dictionary
Y = length of longest word in dictionary

Time complexity of using a set instead of a trie tree

We are doing a 4-child DFS traversal of depth N*M (worst case is traversing entire board). -> 4^(NM)
We are doing this N*M times since we need to check for words starting at each position in the board
-> O(4^(NM)*NM)
Time complexity of using the trie tree

We are doing a 4-child DFS traversal.
The worst case depth in this case is the minimum of [traversing the entire board, traversing until we hit the end of a word].
-> O of each traversal is4^(min(Y, NM))
Note: min accounts for the case where we have words in the dictionary longer than the number of characters in the board itself.
We are doing this N*M times since we need to check for words starting at each position in the board
-> O(4^(min(Y, NM))*NM)
'''


class Node:
    def __init__(self):
        self.word, self.children = None, {}


class Solution:
    def findWords(self, A: List[List[str]], words: List[str]) -> List[str]:
        if not A:
            return []

        # build trie
        root = Node()
        for w in set(words):
            curr = root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = Node()
                curr = curr.children[c]
            curr.word = w

        m, n = len(A), len(A[0])

        res = []

        def dfs(i, j, curr):
            if curr.word:
                res.append(curr.word)
                curr.word = None
            if i < 0 or i >= m or j < 0 or j >= n or A[i][j] not in curr.children:
                return
            c = A[i][j]
            A[i][j] = '#'
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(i + di, j + dj, curr.children[c])
            A[i][j] = c

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res