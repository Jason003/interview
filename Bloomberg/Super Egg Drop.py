class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, K + 1):
                '''
                The dp equation is:
dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1,
assume, dp[m-1][k-1] = n0, dp[m-1][k] = n1
the first floor to check is n0+1.
if egg breaks, F must be in [1,n0] floors, we can use m-1 moves and k-1 eggs to find out F is which one.
if egg doesn't breaks and F is in [n0+2, n0+n1+1] floors, we can use m-1 moves and k eggs to find out F is which one.
So, with m moves and k eggs, we can find out F in n0+n1+1 floors, whichever F is.
                '''
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + 1
                if dp[i][j] >= N: return i