# if we need to list all the palindromes subsequence
def allPalindromes(s):
    res = set()

    def judge(s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def dfs(curr, idx):
        if judge(curr) and curr:
            res.add(''.join(curr))
        for i in range(idx, len(s)):
            dfs(curr + [s[i]], i + 1)

    dfs([], 0)
    return res


print("Total palindromic subsequence are : "
      , allPalindromes(str))
