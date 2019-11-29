'''
很简单 reverse linkedlist 各种方法。。分析一下时间空间复杂度，如果linkedlist 很大怎么办
reverse linkedlist 有很多种方法，有的不是o（1），，，，list很大就break into several parts，save  each head pointers

'''
def reverse_print(start, end):
    if start == end:
        return

    slow = fast = start
    while fast.next != end and fast.next.next != end:
        slow = slow.next
        fast = fast.next.next

    reverse_print(slow.next, end)
    print(slow.val)
    reverse_print(start, slow)

reverse_print(root, None)