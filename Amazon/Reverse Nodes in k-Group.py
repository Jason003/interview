# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        cur, pre = head, dummy
        for _ in range(n, k - 1, -k):
            for _ in range(1, k):
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt
            cur, pre = cur.next, cur
        return dummy.next