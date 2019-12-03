def countPS(str):
    N = len(str)

    # Create a 2D array to store the count
    # of palindromic subsequence
    cps = [[0 for i in range(N + 2)] for j in range(N + 2)]

    # palindromic subsequence of length 1
    for i in range(N):
        cps[i][i] = 1

    # check subsequence of length L
    # is palindrome or not
    for L in range(2, N + 1):

        for i in range(N):
            k = L + i - 1
            if (k < N):
                if (str[i] == str[k]):
                    cps[i][k] = (cps[i][k - 1] +
                                 cps[i + 1][k] + 1)
                else:
                    cps[i][k] = (cps[i][k - 1] +
                                 cps[i + 1][k] -
                                 cps[i + 1][k - 1])

                    # return total palindromic subsequence
    return cps[0][N - 1]


# Driver program
str = "abcb"
print("Number of palindromic subsequence are : "
      , countPS(str))


# if we need to list all the palindromes

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
        if judge(curr):
            res.add(''.join(curr))
        for i in range(idx, len(s)):
            dfs(curr + [s[i]], i + 1)

    dfs([], 0)
    return res


print("Total palindromic subsequence are : "
      , allPalindromes(str))
