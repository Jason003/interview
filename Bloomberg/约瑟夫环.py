class node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def creat1(n):
    if n < 0:
        return 0
    if n == 1:
        return node(1)
    else:
        root = node(1)
        tem = root
        for i in range(2, n + 1):
            tem.next = node(i)
            tem = tem.next
        tem.next = root
        return root


def main(n, k):
    if k == 1:
        return n
    root = creat1(n)
    tem = root
    while True:
        for i in range(k - 2):
            tem = tem.next
        tem.next = tem.next.next
        tem = tem.next
        if tem.next == tem:
            break
    return tem.value


if __name__ == '__main__':
    main(10, 3)

def recursion(n, k):
    if n == 1: return 1
    # The position returned by
    # josephus(n - 1, k) is adjusted
    # because the recursive call
    # josephus(n - 1, k) considers
    # the original position
    # k%n + 1 as position 1  
    return (recursion(n - 1, k) + k - 1) % n + 1

for i in range(2, 800):
    assert main(i, i // 2) == recursion(i, i // 2)