'''
There are several ways to improve the naive dfs method:
(1) memo using hashmap (like the one above)
(2) DP
(3) preprocess the string using word break I DP array to determine whether to go on or not
(4) precompute the max length of all words in the dictionary to reduce the number of recursive calls.
These are all good approaches when not all combinations are valid,
but won't change the time complexity O(2^n) in the worse case scenario
where all combinations of the string are correct (e,g, s=aaa, dic=[a, aa, aaa]).
Some might argue that they reduce the number of recursive/iterative calls
to n^2 using memo or DP just like word break I.
However, the time complexity of each recursive call in this approach is not linear anymore.
Imagine the length of sublist is 2^(n-1).
Optimization only happens when the return value is a integer or boolean.
This is why we don't use DP/memo to solve subsets/permutation problem because all combinations are valid.
'''
def wordBreak(s, wordDict):
    lengths = set(map(len, wordDict))
    wordDict = set(wordDict)
    mem = {}
    def helper(idx, s):
        if idx == len(s):
            return ['']
        if idx in mem:
            return mem[idx]
        res = []
        for length in lengths:
            word = s[idx: idx + length]
            if word in wordDict:
                res += [(word + ' ' + s).strip() for s in helper(idx + length, s)]
        mem[idx] = res
        return res
    return helper(0, s)

