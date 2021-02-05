# -*- coding: utf-8 -*-
# @Time : 2020/12/11 9:55
# @Author : Jiefan
'''
Fine the path from left to right which has the highest minimum sharpness. 路径必须是从左往右，先有个起始点，然后每次要往右上，正右或右下跳一步
[5, 7, 2]
[7, 5, 8]
[9, 1, 5]
在这个例子中，理想路径是.7->.7->.8因为这条路径中的最小值.7在所有路径中最 大。只需要返回这个值，不需要返回路径。这是道dp问题
'''
def minMax(A): # if we can change the value of A, O(1) space
    if not A or not A[0]:
        raise Exception('Invalid Input')
    m, n = len(A), len(A[0])
    res = -float('inf')
    for j in range(1, n):
        for i in range(0, m):
            A[i][j] = min(A[i][j], max(A[i - 1][j - 1] if i > 0 else -float('inf'), A[i + 1][j - 1] if i < m - 1 else -float('inf'), A[i][j - 1]))
            if j == n - 1:
                res = max(res, A[i][j])
    return res
A = [
    [5, 7, 2],
    [7, 5, 8],
    [9, 1, 5]
]
print(minMax(A), A)
def minMax2(A): # if we can't change the value of A, O(1) space
    if not A or not A[0]:
        raise Exception('Invalid Input')
    m, n = len(A), len(A[0])
    dp = list(list(zip(*A))[0])
    print(dp)
    for j in range(1, n):
        temp = [0] * m
        for i in range(0, m):
            temp[i] = min(A[i][j], max(dp[i - 1] if i > 0 else -float('inf'), dp[i + 1] if i < m - 1 else -float('inf'), dp[i]))
        dp = temp
    return max(dp)
A = [
    [5, 7, 2],
    [7, 5, 8],
    [9, 1, 5]
]
print(minMax2(A))