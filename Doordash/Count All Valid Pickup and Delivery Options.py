def validPickDelivery(A):
    picks = set()
    seen = set()
    for s in A:
        if s[0] == 'D':
            pick = 'P' + s[1:]
            if pick not in picks:
                return False
            picks.remove(pick)
        elif s[0] == 'P':
            if s in seen: return False
            seen.add(s)
            picks.add(s)
        else:
            return False
    return len(picks) == 0

'''
Given n orders, each order consist in pickup and delivery services.

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).

Since the answer may be too large, return it modulo 10^9 + 7.
'''

'''
method 1:
Assume we have already n - 1 pairs, now we need to insert the nth pair.
To insert the first element, there are n * 2 - 1 chioces of position。
To insert the second element, there are n * 2 chioces of position。
So there are (n * 2 - 1) * n * 2 permutations.
Considering that delivery(i) is always after of pickup(i), we need to divide 2.
So it's (n * 2 - 1) * n.

method2:
The total number of all permutation obviously eauqls to (2n)!.
For each pair, the order is determined, so we need to divide by 2.
So the final result is (2n)!/(2^n)
'''
import math
def countOrders(n) -> int:
    curr = 1
    for i in range(1, n + 1):
        curr = curr * (i * 2) * (i * 2 - 1) // 2 % (10 ** 9 + 7)
    return curr

def countOrders(n):
    return (math.factorial(n * 2) >> n) % (10**9 + 7)



def generateValidOrders(n):
    res = []
    def dfs(picks, deliveries, curr):
        if len(picks) == len(deliveries) == n:
            res.append(curr)
        for i in range(1, n + 1):
            if i not in picks:
                dfs(picks | {i}, deliveries, curr + ['P' + str(i)])
            if i in picks and i not in deliveries:
                dfs(picks, deliveries | {i}, curr + ['D' + str(i)])
    dfs(set(), set(), [])
    return res

for n in range(1, 100):
    print(n, countOrders(n), countOrders(n) == len(generateValidOrders(n)))


