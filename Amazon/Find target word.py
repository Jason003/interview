'''
given list of tuples: [("a", "b"), ("b", "c".....] and a target word: "hello", 要 求 判 断 能 否 ⽤ tuples 的 字 母 组 成 target 。 每 个 tuple 只 能 ⽤ ⼀ 次 ， tuple ⾥ 两 个 字 母 是 ⼆ 选 ⼀。
'''
import collections
def targetWord(l, word):
    ch2idx = collections.defaultdict(set)
    for i, t in enumerate(l):
        ch2idx[t[0]].add(i)
        ch2idx[t[1]].add(i)

    def dfs(idx, seen):
        if idx == len(word):
            return True
        for i in ch2idx[word[idx]]:
            if seen & (1 << i) == 0 and dfs(idx + 1, seen | (1 << i)):
                return True
        return False
    return dfs(0, 0)

l = [('h','o'),('e','a'),('l','l'),('l','d'),('o','e')]
print(targetWord(l, 'hello'))