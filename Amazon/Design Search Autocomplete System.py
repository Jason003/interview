import collections
class Trie:
    def __init__(self):
        self.children = {}
        self.cnt = collections.Counter()


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Trie()
        for s, t in zip(sentences, times):
            curr = self.root
            for c in s:
                if c not in curr.children:
                    curr.children[c] = Trie()
                curr = curr.children[c]
                curr.cnt[s] = t
        self.s = ''

    def addWord(self, w):
        curr = self.root
        for c in w:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
            curr.cnt[w] += 1

    def input(self, ch: str) -> List[str]:
        if ch != '#':
            self.s += ch
        curr = self.root
        for c in self.s:
            if c not in curr.children:
                if ch == '#':
                    self.addWord(self.s)
                    self.s = ''
                return []
            curr = curr.children[c]
        if ch == '#':
            self.addWord(self.s)
            self.s = ''
            return []
        return sorted(list(curr.cnt.keys()), key=lambda x: (-curr.cnt[x], x))[:3]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

'''
1268. Search Suggestions System

Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
'''
class Trie:
    def __init__(self):
        self.sub = {}
        self.suggestion = []
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for product in sorted(products):
            self._insert(product, root)
        return self._search(searchWord, root)
    def _insert(self, product: str, root: Trie) -> None:
        trie = root
        for char in product:
            if char not in trie.sub:
                trie.sub[char] = Trie()
            trie = trie.sub[char]
            trie.suggestion.append(product)
            trie.suggestion.sort()
            if len(trie.suggestion) > 3:
                trie.suggestion.pop()
    def _search(self, searchWord: str, root: Trie) -> List[List[str]]:
        ans = []
        for char in searchWord:
            if root:
                root = root.sub.get(char)
            ans.append(root.suggestion if root else [])
        return ans
'''
Analysis:

Complexity depends on the sorting, the process of building Trie and the length of searchWord. Sorting cost time O(m * n), due to involving comparing String, which cost time O(m) for each comparison, building Trie cost O(m * n). Therefore,
Time: O(m * n + L), space: O(m * n + L * m) - including return list ans, where m = average length of products, n = products.length, L = searchWord.length().

'''