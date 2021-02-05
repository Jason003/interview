# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        curr = head
        while curr and curr.next:
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = dummy.next
            dummy.next = nxt
        return dummy.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res

class Solution:
    def rotateRight(self, head, k):
        if k == 0 or not head: return head
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        k %= l
        if k == 0: return head
        p = head
        for _ in range(l - k - 1):
            p = p.next
        newHead = p.next
        p.next = None
        p = newHead
        while p and p.next:
            p = p.next
        p.next = head
        return newHead
