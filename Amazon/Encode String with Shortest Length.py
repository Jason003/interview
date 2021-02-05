'''
Example 1:

Input: "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
 

Example 2:

Input: "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
 

Example 3:

Input: "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
 

Example 4:

Input: "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
 

Example 5:

Input: "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".
'''
class Solution:
    def encode(self, s: str) -> str:
        # Dynamic programming
        # dp[i][j]: encoding for string s[i : j + 1] with shortest length

        if not s:
            return s

        # create 2d dp with size len(s) * len(s)
        dp = [[s] * len(s) for i in range(len(s))]

        for width in range(1, len(s) + 1):
            # first round: generate dp[0][0], dp[1][1], dp[2][2], ..., dp[n - 1][n - 1]
            # second round: generate dp[0][1], dp[1][2], dp[2][3], ...., dp[n - 2][n - 1]
            # ......
            # last round: generate dp[0][n - 1], which is the return value

            for i in range(0, len(s) - width + 1):
                j = i + width - 1
                if width < 5:
                    dp[i][j] = s[i: j + 1]
                    continue

                substr = s[i: j + 1]
                repIdx = (substr + substr).find(substr, 1)  # start from 1 to skip s itself

                # case1: substr is repeat of some str
                if repIdx < width:
                    dp[i][j] = (str)((int)(width / repIdx)) + '[' + dp[i][
                        repIdx + i - 1] + ']'  # be careful, here use dp[i][repIdx - 1] instead of substr[:repIdx]

                # case2: substr is not a self repeat str, update dp[i][j] with dp[i][k] + dp[k + 1][j]
                else:
                    for k in range(i, j):
                        dp[i][j] = dp[i][k] + dp[k + 1][j] if len(dp[i][k]) + len(dp[k + 1][j]) < len(dp[i][j]) else \
                        dp[i][j]
        return dp[0][-1]