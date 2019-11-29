def numBSTs(n): # given 1 - n, count how many BSTs can be built using these numbers
    if n == 0 or n == 1:
        return 1
    res = 0
    for i in range(1, n + 1):
        res += numBSTs(i - 1) * numBSTs(n - i)
    return res
for i in range(10):
    print(numBSTs(i))
