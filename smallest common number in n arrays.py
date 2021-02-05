def smallest_common_number(lists):
    for l in lists:
        l.sort()
    n = len(lists)
    pointers = [0] * n
    while all(pointers[i] < len(lists[i]) for i in range(n)):
        mx = max(lists[i][pointers[i]] if pointers[i] < len(lists[i]) else -float('inf') for i in range(n))
        flag = True
        for i in range(n):
            if lists[i][pointers[i]] < mx:
                pointers[i] += 1
                flag = False
        if flag:
            return mx
    return -1

print(smallest_common_number([[2,2],[3,2],[3,4,2,1,4,5,1]]))
