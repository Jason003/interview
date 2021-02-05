import collections
def lock(stopList, target):
    stopList = set(stopList)
    if target in stopList or '0000' in stopList: return -1
    if target == '0000': return 0
    seen = {'0000'}
    dq = collections.deque(['0000'])
    step = 0
    while dq:
        sz = len(dq)
        for _ in range(sz):
            curr = dq.popleft()
            l = list(map(int, list(curr)))
            for i in range(len(l)):
                c = l[i]
                l[i] = (c + 1) % 10
                s = ''.join(map(str, l))
                if s == target: return step + 1
                if s not in seen and s not in stopList:
                    seen.add(s)
                    dq.append(s)
                l[i] = (c + 9) % 10
                s = ''.join(map(str, l))
                if s == target: return step + 1
                if s not in seen and s not in stopList:
                    seen.add(s)
                    dq.append(s)
                l[i] = c
        step += 1
    return -1

print(lock(['1023', '2103', '2201'], '2301'))